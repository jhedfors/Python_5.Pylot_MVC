from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Book')
        self.db = self._app.db
    def index(self):
        return self.load_view('Users/login_reg.html')
    def login_form(self):
        info = self.models['User'].login_user(request.form)
        if info:
            alias,active_id =  info
            session['alias'] = alias
            session['active_id'] = active_id
            return redirect('/books')
        else:
            return redirect('/')
    def register_form(self):
        info = self.models['User'].create_user(request.form)
        print info
        return redirect('/books')
    def user_view(self,id):
        reviews = self.models['Book'].show_reviewed_titles(id)
        count = 0
        for review in reviews:
            count+=1
        profile = self.models['User'].show(id)[0]
        return self.load_view('Users/user.html', profile = profile, reviews = reviews, count = count)
    def logout(self):
        session.clear()
        return redirect('/')
