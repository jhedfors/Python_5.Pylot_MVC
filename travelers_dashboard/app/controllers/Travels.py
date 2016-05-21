from system.core.controller import *

class Travels(Controller):
    def __init__(self, action):
        super(Travels, self).__init__(action)
        self.load_model('Travel')
        self.db = self._app.db
    def travels_view(self):
        my_trips = self.models['Travel'].show_my_trips(session['active_id'])
        other_trips = self.models['Travel'].show_other_trips(session['active_id'])
        return self.load_view('travels.html', my_trips = my_trips, other_trips=other_trips )
    def add_trip_view(self):
        return self.load_view('add_trip.html')
    def destination_view(self,id):
        destination = self.models['Travel'].show_destination(id)[0]
        attendees = self.models['Travel'].show_destination_attendees(id)
        print attendees
        return self.load_view('destination.html', destination = destination, attendees = attendees)
    def add_destination(self):
        info = self.models['Travel'].add_destination(request.form)
        print info
        if 'errors' in info:
            flash(info)
            return redirect('/travels/add')
        else:
            return redirect('/travels')
    def join_trip(self,id):
        self.models['Travel'].join_trip(id, session['active_id'])
        return redirect('/travels')
