
from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
    def index(self):
        return self.load_view('index.html')
    def survey_form(self):
        info = {'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comment' : request.form['comment']}
        session['info'] = info
        return redirect('/result')

    def result_view(self):
        info = session['info']
        return self.load_view('result.html',info=info)
