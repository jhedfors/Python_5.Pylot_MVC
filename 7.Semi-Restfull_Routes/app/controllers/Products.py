from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db
    def index(self):
        return redirect('/products')
    def index_view(self):
        products = self.models['Product'].index()
        return self.load_view('index.html', products = products)
    def show_view(self, id):
        product = self.models['Product'].show(id)[0]
        return self.load_view('view.html', product = product)
    def new_view(self):
        return self.load_view('new.html')
    def edit_view(self, id):
        product = self.models['Product'].show(id)[0]
        return self.load_view('edit.html', product = product)
    def create(self, methods='POST'):
        info = request.form
        self.models['Product'].add(info)
        return redirect('/products')
    def destroy(self,id):
        self.models['Product'].delete(id)
        return redirect('/products')
    def update(self, methods='POST'):
        info = request.form
        self.models['Product'].update(info)
        return redirect('/products')
