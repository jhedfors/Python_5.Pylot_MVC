from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        # self.load_model('WelcomeModel')
        self.db = self._app.db


    def index(self):

        return self.load_view('Users/login_reg.html')
