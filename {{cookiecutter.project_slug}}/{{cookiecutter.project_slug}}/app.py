from webob import exc
from waitress import serve


class WSGIApplication:
    def __call__(self, environ, start_response):
        response = exc.HTTPNotFound()
        return response(environ, start_response)


if __name__ == "__main__":
    host, port = "localhost", 3000
    serve(WSGIApplication(), host=host, port=port)
