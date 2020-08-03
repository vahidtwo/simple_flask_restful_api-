from flask import request, jsonify

from main import db
from post import post_blueprint, Post


@post_blueprint.route('/', methods=['GET'])
def get_all_post():
    posts = Post.query.all()
    posts = [
        {
            'id': post.id,
            'title': post.title,
            'body': post.body
        } for post in posts
    ]
    return jsonify(posts), 200


@post_blueprint.route('/', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
        post = Post(title=data['title'], body=data['body'])
        db.session.add(post)
        db.session.commit()
        return {'success': True}, 201
    except Exception as e:
        db.session.rollback()
        return {'success': False}, 500


@post_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id_post(id):
    try:
        post = Post.query.get(Post.id == id)
        return jsonify({'id': post.id, 'title': post.title, 'body': post.body}), 200
    except Exception as e:
        db.session.rollback()
        return {'success': False}, 500


@post_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_by_id_post(id):
    try:
        post = Post.query.filter_by(id == id).first_or_404()
        db.session.delete(post)
        db.session.commit()
        return jsonify({'id': post.id, 'title': post.title, 'body': post.body})
    except Exception as e:
        db.session.rollback()
        return {'success': False}, 500


@post_blueprint.route('/<int:id>', methods=['PUT'])
def delete_by_id_post(id):
    try:
        data = request.get_json()
        post = Post.query.filter_by(id == id).first_or_404()
        post.title = data['title'] if data.get('title') else post.title
        post.body = data['body'] if data.get('body') else post.body
        db.session.commit()
        return jsonify({'success': True, 'data': {'id': post.id, 'title': post.title, 'body': post.body}}), 200
    except Exception as e:
        db.session.rollback()
        return {'success': False}, 500
