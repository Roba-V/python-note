import os
from datetime import datetime
from wsgiref.simple_server import make_server

import sqlalchemy as sa
import sqlalchemy.orm as orm
from docutils.core import publish_parts
from jinja2 import Environment
from jinja2.loaders import PackageLoader
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from webdispatch.urldispatcher import URLDispatcher
from webob.dec import wsgify
from webob.exc import HTTPFound
from webob.static import DirectoryApp

here = os.path.dirname(__file__)

Base = declarative_base()
DBSession = orm.scoped_session(orm.sessionmaker())

env = Environment(loader=PackageLoader(__name__, 'templates'))


class Page(Base):
    __tablename__ = 'pages'
    id = sa.Column(sa.Integer, primary_key=True)
    page_name = sa.Column(sa.Unicode(255), unique=True)
    contents = sa.Column(sa.UnicodeText)
    created = sa.Column(sa.DateTime, default=datetime.now)
    edited = sa.Column(sa.DateTime, onupdate=datetime.now)

    @property
    def html_contents(self):
        parts = publish_parts(source=self.contents, writer_name='html')
        return parts['html_body']


def init_db(engine):
    DBSession.configure(bind=engine)
    Base.metadata.create_all(bind=DBSession.bind)
    try:
        front_page = Page(page_name='FrontPage', contents="""\
FrontPage
==============""")
        DBSession.add(front_page)
        DBSession.commit()
    except IntegrityError:
        DBSession.remove()


@wsgify.middleware
def sqla_transaction(req, app):
    try:
        res = req.get_response(app)
        DBSession.commit()
        return res
    finally:
        DBSession.remove()


@wsgify
def page_view(request):
    page_name = request.urlvars['page_name']
    # edit_url = request.environ['webdispatch.urlgenerator'] \
    #     .generate('page_edit', page_name=page_name)
    page = DBSession.query(Page).filter(Page.page_name == page_name).one()
    tmpl = env.get_template('page.html')
    return tmpl.render(page=page)


def make_app():
    application = URLDispatcher()
    js_app = DirectoryApp(os.path.join(here, 'static/js'))
    css_app = DirectoryApp(os.path.join(here, 'static/css'))
    img_app = DirectoryApp(os.path.join(here, 'static/img'))

    application.add_url('js', '/js/*', js_app)
    application.add_url('css', '/css/*', css_app)
    application.add_url('img', '/img/*', img_app)
    application.add_url('page', '/{page_name}', page_view)
    application.add_url('top', '/', HTTPFound(location='FrontPage'))

    application = sqla_transaction(application)
    return application


def main():
    engine = sa.create_engine('sqlite:///{dir}/wiki.db'.format(dir=os.getcwd()))
    init_db(engine)
    application = make_app()
    httpd = make_server('', 8000, application)
    httpd.serve_forever()
