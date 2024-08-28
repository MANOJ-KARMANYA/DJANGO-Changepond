from django.urls import path
from . import views

urlpatterns = [
    path('Index', views.land_page,name = 'land_page'),
    path('Post-Detail/<slug:card_id>', views.detail_page,name = 'detail_page'),
    path('All-Posts', views.second_page,name = 'second_page'),
    path("forms", views.CreateProfileView.as_view(), name='post_create'),
    path("success", views.success, name='success'),
]