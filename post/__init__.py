from flask import Blueprint

post_blueprint = Blueprint('post', __name__, url_prefix='/post/')
from .models.post import Post
from post.api.v1.crud_test import *

