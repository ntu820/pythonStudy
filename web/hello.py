#def application(environ, start_response):
#start_response('200 OK', [('Content-Type', 'text/html')])
#return [b'<h1>Hello, web!</h1>']

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'WEB')
	return [body.encode('utf-8')]


