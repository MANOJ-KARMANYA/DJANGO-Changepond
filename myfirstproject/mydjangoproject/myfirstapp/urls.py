from django.urls import path
from .views import land_page,second_page,detail_page

urlpatterns = [
    path('Index', land_page,name = 'land_page'),
    path('Post-Detail/<int:card_id>', detail_page,name = 'detail_page'),
    path('All-Posts', second_page,name = 'second_page'),
]