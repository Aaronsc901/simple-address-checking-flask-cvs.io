from flask import request, render_template
from models import Post
from .run import public_nc 

@public_nc.route('/')
def index():
    return render_template('public/index.html')

@public_nc.route("/post/", methods=['POST'])
def uploader(): 
	if 'archivo' in request.files: 
		file = request.files['archivo']
		post = Post.one(file)
		#Debo averiguar como acceder a estos datos desde aqui o en
		# el propio html
		return render_template("public/result.html", post=post)

	