from system.core.controller import *
import random
import string

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

        # self.load_model('WelcomeModel')
        # self.db = self._app.db
    def index(self):
        return self.load_view('main.html')
    def random(self, methods=['GET']):
       	test = ''.join(random.choice(string.ascii_uppercase) for x in range(14))
       	if 'counter' not in session :
       		session['counter'] = 1
       	else :
       		session['counter'] += 1
    	return self.load_view('main.html', test = test)
