from django.urls import path,include
from . import views

urlpatterns = [

    path('<int:week>', views.week_details_by_number),  #1
    path('<str:week>', views.week_details, name='week-details')
    
    
]

# <placeholder>

# month/1 --> month/January
# month/2 --> month/Feb
