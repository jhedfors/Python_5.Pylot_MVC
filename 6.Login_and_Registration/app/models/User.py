from system.core.model import Model
# from flask.ext.bcrypt import Bcrypt
import re
# bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)(.{8,})$')
class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def register(self,post):
        errors = {}
        if len(post['fname'])< 2:
            errors['fname_error'] = u'First Name cannot be empty!'
        elif not NAME_REGEX.match(post['fname']):
            errors['fname_error'] = u"Invalid First Name!"
        if len(post['lname'])< 2:
            errors['lname_error'] = u'Last Name cannot be empty!'
        elif not NAME_REGEX.match(post['lname']):
            errors['lname_error'] = u"Invalid Last Name!"
        if len(post['email'])< 1:
            errors['email_error'] = u'Email cannot be empty!'
        elif not EMAIL_REGEX.match(post['email']):
            errors['email_error'] = u"Invalid Email Address!"
        if len(post['password'])< 1:
            errors['password_error'] = u'Password cannot be empty!'
        elif not PASSWORD_REGEX.match(post['password_conf']):
            errors['password_error'] = u"Password must be at least 8 characters,and contain at least 1 uppercase letter and one number!"
        if len(post['password_conf'])< 1:
            errors['password_conf_error'] = u'Password Confirmation cannot be empty!'
        elif not PASSWORD_REGEX.match(post['password_conf']):
            errors['password_conf_error'] = u"Invalid Email Address!"
        if not post['password_conf'] == post['password']:
            errors['password_conf_error'] = u"Password and Confirmation must match!"
        if len(errors) > 0:
            return errors
        pw_hash = self.bcrypt.generate_password_hash(post['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_date, modified_date) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {'first_name' : post['fname'],'last_name' : post['lname'],'email' : post['email'],'password' : pw_hash}
        self.db.query_db(query,data)
        return False
    def login(self,post):
        errors = {}

        if len(post['email'])< 1:
            errors['login_email_error'] = u'Email cannot be empty!'
        elif not EMAIL_REGEX.match(post['email']):
            errors['login_email_error'] = u"Invalid Email Address!"
        if len(post['password'])< 1:
            errors['login_password_error'] = u'Password cannot be empty!'
        info = {'errors': errors}
        if len(errors) > 0:
            return info

        query = "SELECT id, first_name, password FROM users WHERE email = :email"
        data = {'email' : post['email']}
        db = self.db.query_db(query,data)[0]
        match = self.bcrypt.check_password_hash(db['password'], post['password'])
        if(db):
            if(match):
                return {'record': db}
            else:
                errors['login_password_error'] = u'Invalid Email or Password!'
                return {'errors': errors}
