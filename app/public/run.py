from flask import Blueprint

public_nc = Blueprint('public', __name__, template_folder='templates')

from . import routes



