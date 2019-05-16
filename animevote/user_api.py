from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from animevote.models import User


class UserList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.username != 'admin':
            return {'message': 'you are not administrator.'}
        users = User.get_user_list()
        return [u.as_dict() for u in users]


def min_length_str(min_length):
    def validate(s):
        if s is None:
            raise Exception('password required')
        if not isinstance(s, (int, str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception("String must be at least %i characters long" % min_length)

    return validate


class UserApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=min_length_str(5), required=True, help='{error_msg}'
    )

    parser.add_argument(
        'email', type=str, required=True, help='email required'
    )

    def get(self, username):
        user = User.get_by_username(username)
        if user:
            return user.as_dict()
        return {'message': 'user not found'}, 404

    def post(self, username):
        data = UserApi.parser.parse_args()
        user = User.get_by_username(username)
        if user:
            return {'message': 'user already exist'}
        user = User(
            username=username,
            email=data['email']
        )
        user.set_password(data['password'])
        user.add()
        return user.as_dict(), 201


    def delete(self, username):
        user = User.get_by_username(username)
        if user:
            user.delete()
            return {'message': 'user deleted'}
        else:
            return {'message': 'user not found'}

    def put(self, username):
        user = User.get_by_username(username)
        if user:
            data = User.parser.parse_args()
            user.password_hash = data['password']
            user.update()
            return user.as_dict()
        return {'message': 'user not found'}, 204
