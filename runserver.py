# app as application for wsgi
from recipes import app as application

if __name__ == '__main__':
	application.run(debug=True)