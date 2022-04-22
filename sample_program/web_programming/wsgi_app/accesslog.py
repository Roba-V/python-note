class Middleware:

    def __init__(self, app, logger):
        self.app = app
        self.logger = logger

    def __call__(self, environ, start_response):
        request_method = environ['REQUEST_METHOD']
        path = environ.get('SCRIPT_NAME', '') + environ.get('PATH_INFO', '')
        self.logger.info('access %s %s', request_method, path)
        return self.app(environ, start_response)
