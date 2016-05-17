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
        return self.load_view('Users/create.html')
    def register_form(self):
        admin_count = self.models['User'].show_admin_count()[0]['count']
        user_level = 'normal'
        if admin_count == 0:
            user_level = 'admin'
        info = self.models['User'].add(request.form, user_level)
        if 'errors' in info:
            flash(info['errors'])
            return redirect('/register')
        elif 'active_id' in session:
            return redirect('/dashboard')
        else:
            session['active_id'] = info['active_id']
            session['user_level'] = user_level
            return redirect('/dashboard')
    def signin_form(self):
        info = self.models['User'].signin(request.form)
        if 'errors' in info:
            flash(info['errors'])
            return redirect('/signin')
        else:
            session['active_id'] = info['active_id']
            session['user_level'] = info['user_level']
            if session['user_level'] == 'admin':
                return redirect('/dashboard/admin')
            return redirect('/dashboard')
    def dashboard_view(self):
        info = self.models['User'].index()
        return self.load_view('Users/dashboard.html', users = info)
    def dashboard_view_admin(self):
        info = self.models['User'].index()
        return self.load_view('Users/dashboard.html', users = info)
    def create_view(self):
        return self.load_view('Users/create.html')
    def show_view(self,id):
        info = self.models['User'].show(id)[0]
        messages = self.models['Message'].show(id)
        return self.load_view('Users/show.html', profile = info, messages = messages)
    def edit_view(self):
        active_id = session['active_id']
        info = self.models['User'].show(active_id)[0]
        return self.load_view('Users/profile.html', profile = info)
    def edit_view_admin(self, id):
        info = self.models['User'].show(id)[0]
        return self.load_view('Users/edit.html', profile = info)
    def edit_form(self):
        info = self.models['User'].update(request.form)
        return redirect('/dashboard')
    def edit_description_form(self):
        info = self.models['User'].update_description(request.form)
        return redirect('/dashboard')
    def edit_password_form(self):
        info = self.models['User'].update_password(request.form)
        return redirect('/dashboard')
    def delete_user(self,id):
        self.models['User'].delete(id)
        return redirect('/dashboard')
    def logoff(self):
        session.clear()
        return redirect('/')
