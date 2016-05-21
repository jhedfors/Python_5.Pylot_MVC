from system.core.model import Model
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)(.{8,})$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def login(self,post):
        errors = {}
        if len(post['username'])< 1:
            errors['login_username'] = u'Username cannot be empty!'
        if len(post['password'])< 1:
            errors['login_password'] = u'Password cannot be empty!'
        if len(errors) > 0:
            return {'errors': errors}
        query = "SELECT id, name, password FROM users WHERE username = :username"
        values = {'username': post['username']}
        db = self.db.query_db(query,values)
        if(db):
            db = db[0]
            match = self.bcrypt.check_password_hash(db['password'],post['password'])
            if(match):
                return {'active_id': db['id'], 'name': db['name']}
        errors['login_password'] = u'Invalid Email or Password!'
        return {'errors': errors}

    def register(self,post):
        errors = {}
        if len(post['name'])< 3:
            errors['name'] = u'Name cannot be empty!'
        if len(post['username'])< 3:
            errors['username'] = u'Username cannot be empty!'
        if not PASSWORD_REGEX.match(post['password']):
            errors['password'] = u"Password must be at least 8 characters,and contain at least 1 uppercase letter and one number!"
        if not post['confirm_password'] == post['password']:
            errors['confirm_password'] = u"Password and Confirmation must match!"
        if(self.show(post['username'])):
            errors['username'] = u"Username already exists!"
        if len(errors) > 0:
            return {'errors': errors}
        pw_hash = self.bcrypt.generate_password_hash(post['password'])
        query = "INSERT INTO users (name, username, password, created_at, modified_at) VALUES (:name, :username, :password, NOW(), NOW())"
        values = {'name' : post['name'], 'username': post['username'], 'password': pw_hash}
        active_id = self.db.query_db(query,values)
        return {'active_id': active_id}
    def show(self, username):
        query = "SELECT username FROM users WHERE username = :username"
        values = {'username':username}
        return self.db.query_db(query,values)
