
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/register'] = 'Users#register'
routes['POST']['/login'] = 'Users#login'
routes['GET']['/travels'] = 'Travels#travels_view'
routes['GET']['/travels/add'] = 'Travels#add_trip_view'
routes['GET']['/join_trip/<int:id>'] = 'Travels#join_trip'
routes['GET']['/travels/destination/<id>'] = 'Travels#destination_view'
routes['POST']['/add_destination'] = 'Travels#add_destination'
routes['GET']['/logout'] = 'Users#logout'
