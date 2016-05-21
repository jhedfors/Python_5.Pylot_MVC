from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db
    def index(self):
        return self.load_view('login_reg.html')
    def login(self):
        info = self.models['User'].login(request.form)
        info['login_form'] = request.form
        if 'errors' in info:
            flash(info)
            return redirect('/')
        session['active_id'] = info['active_id']
        session['name'] = info['name']
        return redirect('/travels')
    def register(self):
        info = self.models['User'].register(request.form)
        info['reg_form'] = request.form
        print info
        if 'errors' in info:
            flash(info)
            return redirect('/')
        session['active_id'] = info['active_id']
        session['name'] = request.form['name']
        return redirect('/travels')
    def logout(self):
        session.clear()
        return redirect('/')
