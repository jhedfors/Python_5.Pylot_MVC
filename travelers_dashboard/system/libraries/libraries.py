def initialize_libraries(app):
    #add custom filters and library elements here for now
    #e.g custom date filter
    @app.template_filter('customDate')
    def customDate(s):
        if int(s.strftime('%d')) == 1 or int(s.strftime('%d')) == 31:
            return s.strftime('%b %dst %Y %I:%M%p')
        if int(s.strftime('%d')) > 3:
        #   return s.strftime('%b %dth %Y %-I:%M%p')
            return s.strftime('%b %dth %Y %I:%M %p')
        if int(s.strftime('%d')) == 3:
            return s.strftime('%b %drd %Y %I:%M%p')
        if int(s.strftime('%d')) == 2:
            return s.strftime('%b %dnd %Y %I:%M%p')
        # Example usage {{date_object | customDate}}
    @app.template_filter('myDate')
    def myDate(s):
        return s.strftime('%b %d %Y %I:%M %p')
    @app.template_filter('smallDate')
    def smallDate(s):
        return s.strftime('%b %d %Y')
