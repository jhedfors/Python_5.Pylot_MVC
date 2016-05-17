from system.core.controller import *

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        self.load_model('Message')
        self.load_model('Comment')
        self.db = self._app.db
    def message_form(self):
        post = request.form
        self.models['Message'].add(post)
        return redirect('/users/show/'+post['recip_id'])
    def comment_form(self):
        post = request.form
        self.models['Message'].add_comment(post)
        return redirect('/users/show/'+post['recip_id'])
    def show_comments(self,id):
        self.models['Comment'].show(id)
