from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')
        self.db = self._app.db
    def index(self):
        return self.load_view('Users/welcome.html')
    def signin_view(self):
        return self.load_view('Users/signin.html')
    def register_view(self):
        return self.load_view('Users/register.html')
    def register_form(self):
        info = self.models['User'].add(request.form)
        return redirect('/dashboard')
    def dashboard_view(self):
        info = self.models['User'].index()
        return self.load_view('Users/dashboard.html', users = info)
    def dashboard_view_admin(self):
        return self.load_view('Users/dashboard.html')
    def create_view(self):
        return self.load_view('Users/create.html')
    def show_view(self, id = None):
        return self.load_view('Users/show.html')
    def edit_view(self):
        info = self.models['user'].show()
        return self.load_view('Users/edit.html')
    def edit_view_admin(self, id):
        info = self.models['User'].show(id)[0]
        print info
        return self.load_view('Users/edit.html', profile = info)
    def logoff(self):
        return redirect('/')
