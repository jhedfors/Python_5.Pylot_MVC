
from system.core.model import Model
from datetime import datetime
import time
class Travel(Model):
    def __init__(self):
        super(Travel, self).__init__()
    def add_destination(self,post):
        errors = {}
        print post
        if len(post['destination'])< 1:
            errors['destination'] = u'Destination cannot be empty!'
        if len(post['description'])< 1:
            errors['description'] = u'Description cannot be empty!'
        if len(post['start_date'])< 1:
            errors['start_date'] = u'Start Date cannot be empty!'
        elif datetime.strptime(post['start_date'], "%Y-%m-%d") < datetime.now():
            errors['start_date'] = u'Start Date cannot be in the past!'
        if len(post['end_date'])< 1:
            errors['end_date'] = u'End Date cannot be empty!'
        elif datetime.strptime(post['start_date'], "%Y-%m-%d") > datetime.strptime(post['end_date'], "%Y-%m-%d"):
            errors['end_date'] = u'End Date cannot be before Start Date!'
        if len(errors) > 0:
            return {'errors': errors}
        query = "INSERT INTO destinations (user_planner_id, destination, description, start_date, end_date,created_at, modified_at) VALUES (:user_planner_id,:destination, :description, :start_date, :end_date, NOW(),NOW())"
        values ={'user_planner_id':post['active_id'],'destination' :post['destination'], 'description':post['description'], 'start_date':post['start_date'],'end_date' :post['end_date']}
        return {self.db.query_db(query,values)}


    # def future_date_check(str):
	# 	if str< date("Y-m-d"):
	# 		return False
	# 	return True
    #
	# def return_date_check(start,end):
	# 	if date(end)< date(start):
	# 		return False
	# 	return True


    def show_my_trips(self, active_id):
        query = "SELECT users.name, destination, destinations.id AS dest_id, start_date, end_date, description FROM destinations LEFT JOIN schedules ON destinations.id = schedules.destination_id LEFT JOIN users ON users.id = schedules.user_id LEFT JOIN users AS planners ON planners.id = destinations.user_planner_id WHERE users.id = :active_id or planners.id = :active_id"
        values ={'active_id':active_id}
        return self.db.query_db(query,values)
    def show_other_trips(self,active_id):
        query = "SELECT planners.name AS planner, destination, destinations.id AS dest_id, start_date, end_date, description FROM destinations LEFT JOIN schedules ON destinations.id = schedules.destination_id LEFT JOIN users ON users.id = schedules.user_id LEFT JOIN users AS planners ON planners.id = destinations.user_planner_id WHERE NOT destinations.id IN(SELECT destinations.id FROM destinations LEFT JOIN schedules ON destinations.id = schedules.destination_id LEFT JOIN users ON users.id = schedules.user_id LEFT JOIN users AS planners ON planners.id = destinations.user_planner_id WHERE users.id = :active_id or planners.id = :active_id)"
        values ={'active_id':active_id}
        return self.db.query_db(query,values)

    def show_destination(self, id):
        query = "SELECT users.name AS planner_name, destinations.destination, description, start_date, end_date FROM users LEFT JOIN destinations ON destinations.user_planner_id = users.id WHERE destinations.id = :id"
        values = {'id':id}
        return self.db.query_db(query,values)
    def show_destination_attendees(self,id):
        query = "SELECT users.id, users.name FROM destinations LEFT JOIN schedules ON destinations.id = schedules.destination_id LEFT JOIN users ON users.id = schedules.user_id WHERE destinations.id = :id"
        values = {'id':id}
        return self.db.query_db(query,values)

    def join_trip(self,id,active_id):
        query = "INSERT INTO schedules (user_id, destination_id) VALUES (:user_id, :destination_id)"
        values = {'user_id':active_id, 'destination_id' :id}
        return self.db.query_db(query,values)
