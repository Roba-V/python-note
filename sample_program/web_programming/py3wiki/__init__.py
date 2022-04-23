from webdispatch.urldispatcher import URLDispatcher
from wsgiref.simple_server import make_server


def make_app():
    application = URLDispatcher()
    return application


def main():
    application = make_app()
    httpd = make_server('', 8000, application)
    httpd.serve_forever()
