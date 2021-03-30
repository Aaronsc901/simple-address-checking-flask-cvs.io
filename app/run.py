# min3/app/__init__.py
from flask import Flask

def create_app():
	app = Flask(__name__)

	from public.run import public_nc
	app.register_blueprint(public_nc)

	return app
