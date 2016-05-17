from system.core.model import Model
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)(.{8,})$')
class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def signin(self,post):
        errors = {}
        if len(post['email'])< 1:
            errors['email'] = u'Email cannot be empty!'
        elif not EMAIL_REGEX.match(post['email']):
            errors['email'] = u"Invalid Email Address!"
        if len(post['password'])< 1:
            errors['password'] = u'Password cannot be empty!'
        if len(errors) > 0:
            return {'errors': errors}
        query = "SELECT users.id as user_id, email, password, user_level FROM users WHERE email = :email"
        values = {'email': post['email']}
        db = self.db.query_db(query,values)[0]
        match = self.bcrypt.check_password_hash(db['password'],post['password'])
        if(db):
            if(match):
                return {'active_id': db['user_id'], 'user_level': db['user_level']}
            else:
                errors['password'] = u'Invalid Email or Password!'
                return {'errors': errors}

    def add(self,post,user_level):
        errors = {}
        if len(post['first_name'])< 2:
            errors['first_name'] = u'First Name cannot be empty!'
        elif not NAME_REGEX.match(post['first_name']):
            errors['first_name'] = u"Invalid First Name!"
        if len(post['last_name'])< 2:
            errors['last_name'] = u'Last Name cannot be empty!'
        elif not NAME_REGEX.match(post['last_name']):
            errors['last_name'] = u"Invalid Last Name!"
        if len(post['email'])< 1:
            errors['email'] = u'Email cannot be empty!'
        elif not EMAIL_REGEX.match(post['email']):
            errors['email'] = u"Invalid Email Address!"
        if len(post['password'])< 1:
            errors['password'] = u'Password cannot be empty!'
        elif not PASSWORD_REGEX.match(post['password']):
            errors['password'] = u"Password must be at least 8 characters,and contain at least 1 uppercase letter and one number!"
        if len(post['confirm_password'])< 1:
            errors['confirm_password'] = u'Password Confirmation cannot be empty!'
        if not post['confirm_password'] == post['password']:
            errors['confirm_password'] = u"Password and Confirmation must match!"
        if len(errors) > 0:
            return {'errors': errors}
        pw_hash = self.bcrypt.generate_password_hash(post['password'])
        query = "INSERT INTO users (first_name, last_name, description, email, password, user_level, created_on, modified_on) VALUES (:first_name, :last_name,:description, :email, :password, :user_level, NOW(), NOW())"
        values = {'first_name' : post['first_name'], 'last_name': post['last_name'],'description': '', 'email': post['email'], 'password': pw_hash, 'user_level': user_level}
        active_id = self.db.query_db(query,values)
        return {'active_id': active_id}
    def index(self):
        query = "SELECT id as user_id, concat(first_name, ' ',last_name) as name, email, created_on, user_level FROM users"
        return self.db.query_db(query)
    def show(self,id):
        query = "SELECT users.id as user_id, first_name, last_name, email, description, user_level, created_on FROM users WHERE id = :id"
        values = {'id': id}
        return self.db.query_db(query,values)
    def show_admin_count(self):
        query = "SELECT COUNT(users.id) as count FROM users WHERE user_level = :user_level"
        values = {'user_level': 'admin'}
        return self.db.query_db(query,values)
    def update(self, post):
        query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, user_level = :user_level WHERE id = :user_id"
        values = {'first_name' : post['first_name'], 'last_name' : post['last_name'], 'user_level' :post['user_level'], 'email':post['email'], 'user_id':post['user_id']}
        return self.db.query_db(query, values)
    def update_description(self,post):
        print post
        query = "UPDATE users SET description = :description WHERE id = :user_id"
        values = {'description':post['description'],'user_id':post['user_id']}
        return self.db.query_db(query, values)
    def update_password(self,post):
        print post
        query = "UPDATE users SET password = :password WHERE id = :user_id"
        values = {'password':post['password'],'user_id':post['user_id']}
        return self.db.query_db(query, values)
    def delete(self,id):
        query = "DELETE FROM users WHERE id = :id"
        values = {'id': id}
        return self.db.query_db(query, values)
