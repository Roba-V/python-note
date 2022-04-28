from wsgiref.simple_server import make_server
import logging
import accesslog


def hello(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain;charset=utf-8')])

    return [b"Hello, world"]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('access log')
httpd = make_server('', 8080, accesslog.Middleware(hello, logger))
httpd.serve_forever()
