"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200

@api.route('/users', methods=['POST', 'GET'])
def users():

    # get all the people
    user_query = User.query.all()

    # map the results and your list of people  inside of the all_people variable
    all_users = list(map(lambda x: x.serialize(), user_query))

    # get just one person
    # response_body = {
    #     all_users
    # }

    return jsonify(all_users), 200