from django.urls import path,include
from .import views

urlpatterns = [

    path('', views.index),
    path('<int:month>', views.monthly_details_by_number),  #1
    path('<str:month>', views.monthly_details, name='month-details')
    
]

# <placeholder>

# month/1 --> month/January
# month/2 --> month/Feb
