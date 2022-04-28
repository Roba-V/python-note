import urllib.parse
from wsgiref.simple_server import make_server


def greeting(environ, start_response):
    query_string = environ['QUERY_STRING']
    params = urllib.parse.parse_qs(query_string)
    start_response('200 OK', [('Content-type', 'text/plain;charset=utf-8')])

    name = params.get('name', ['world'])[0]
    body = 'Hello, {0}'.format(name)

    return [body.encode('utf-8')]


httpd = make_server('', 8080, greeting)
httpd.serve_forever()
