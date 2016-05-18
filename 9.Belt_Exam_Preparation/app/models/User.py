
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def show(self,id):
        query = "SELECT alias, users.name, email FROM users WHERE id = :user_id"
        values = {'user_id': id}
        return self.db.query_db(query,values)

    def create_user(self, post):
        pw_hash = self.bcrypt.generate_password_hash(post['password'])
        query = "INSERT INTO users (name, alias, email, password, created_at, modified_at) VALUES (:name, :alias, :email, :password, NOW(), NOW())"
        values = {'name':post['name'], 'alias' : post['alias'], 'email' :post['email'], 'password':pw_hash}
        return self.db.query_db(query,values)
    def login_user(self, post):
        query = "SELECT * FROM users WHERE email = :email"
        values = {'email': post['email']}
        db = self.db.query_db(query,values)[0]
        if db:
            match = self.bcrypt.check_password_hash(db['password'],post['password'])
            if match:
                return db['alias'],db['id']
        return False
