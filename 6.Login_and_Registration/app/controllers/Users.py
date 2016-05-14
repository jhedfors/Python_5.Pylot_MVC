from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
    def index(self):

        return self.load_view('login_reg.html')
    def registration_form(self):
        errors = self.models['User'].register(request.form)
        if errors:
            flash(errors)
            return redirect('/')
        print request.form
        session['first_name'] = request.form['fname']
        return redirect('/success')
    def login_form(self):
        info = self.models['User'].login(request.form)
        if 'errors' in info:
            flash(info['errors'])
            return redirect('/')
        if 'record' in info:
            session['first_name'] = info['record']['first_name']
            return redirect('/success')
    def success_view(self):
        return self.load_view('success.html')
