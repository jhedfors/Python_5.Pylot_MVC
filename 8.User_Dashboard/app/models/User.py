from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def add(self,post):
        print post
        query = "INSERT INTO users (first_name, last_name, description, email, password, user_level, created_on, modified_on) VALUES (:first_name, :last_name,:description, :email, :password, :user_level, NOW(), NOW())"
        values = {'first_name' : post['first_name'], 'last_name': post['last_name'],'description': '', 'email': post['email'], 'password': post['password'], 'user_level':'normal'}
        return self.db.query_db(query,values)
    def index(self):
        query = "SELECT id as user_id, concat(first_name, ' ',last_name) as name, email, created_on, user_level FROM users"
        return self.db.query_db(query)
    def show(self,id):
        query = "SELECT first_name, last_name, email, description, user_level FROM users WHERE id = :id"
        values = {'id': id}
        return self.db.query_db(query,values)
