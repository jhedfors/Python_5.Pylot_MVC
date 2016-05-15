from system.core.controller import *

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)

        self.load_model('Message')
        self.db = self._app.db


    def index(self):

        return self.load_view('index.html')
