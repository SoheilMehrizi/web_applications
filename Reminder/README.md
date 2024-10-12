# Reminder
Writing A Restful Reminder app that Reminds By Email
** RestFul
** Having A Scout for Check the Upcoming Events and Cleaning the Buffer
## models.py
** Event : Storing the Events

## serializers.py
** Event_Serializer : Serialize the Event Model for the RestApi viewset

## views.py
** EventViewSet : viewset / hadled_methods = ['get', 'post', 'put', 'delete']
  ### Methods:
    ** def _get_upcomings
      get the upcoming Events every minute
**ReminderAPI
  ### Methods :
    ** get :
        get sorted list of upcoming reminders
    ** post: 
         get the Upcoming events from the EventViewSet._get_upcomings
    **_clear:
        clean the Buffer Every 10 minutes
