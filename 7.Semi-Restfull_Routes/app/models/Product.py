from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    def index(self):
        query = "SELECT id, name, description, price FROM products"
        values = {}
        return self.db.query_db(query,values)
    def show(self,id):
        query = "SELECT id, name, description, price FROM products WHERE id = :id"
        values = {'id' : id}
        return self.db.query_db(query,values)
    def add(self,post):
        query = "INSERT INTO products (name, description, price, created_at, modified_at) VALUES(:name, :description, :price, NOW(), NOW())"
        values = {'name': post['name'],'description': post['description'],'price': post['price']}
        item = self.db.query_db(query,values)
        return item
    def delete(self,id):
        query = "DELETE FROM products WHERE id = :id"
        values = {'id' : id}
        return self.db.query_db(query,values)
    def update(self,post):
        query = "UPDATE products SET name = :name, description= :description, price = :price, modified_at = NOW() WHERE id = :id"
        values = {'name': post['name'],'description': post['description'],'price': post['price'],'id' : post['id']}
        item = self.db.query_db(query,values)
        return item
