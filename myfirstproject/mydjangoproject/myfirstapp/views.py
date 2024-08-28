from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import *
# Create your views here.
from datetime import datetime


# def land_page(request):

#     section_name = 'My First Django Project'
#     return render(request, 'cardsdetail/index.html', {'section_name': section_name, 'cards': cards_data})

# def second_page(request):
#     return render(request, 'includes/cards.html', {'cards': cards_data})

# def detail_page(request, card_id):
#     for c in cards_data:
#         if c['id'] == int(card_id):
#             card = c
#     return render(request, 'cardsdetail/detail.html', {'card': card})


cards_data = Posts.objects.all()

def land_page(request):

    section_name = 'My First Django Project'

    context = {
        'show_all': False, 
        'section_name': section_name, 
        'cards': cards_data
    }
    return render(request,"cardsdetail/index.html",context)

def second_page(request):
    context = {
        'show_all': True, 
        'cards': cards_data
    }
    return render(request,"cardsdetail/allpost.html",context)


def detail_page(request, card_id):

    cards_data = Posts.objects.filter(slug=card_id)
    return render(request, 'cardsdetail/detail.html', {"cards": cards_data})
    # return render(request, 'cardsdetail/detail.html', {"card": cards_data[0]})
#we can try converting the querryset to dictionary 


def form(request):
    return render(request,"cardsdetail/form.html",{
                      "postdata":cards_data
                   })


class CreateProfileView(CreateView):
    model = Posts
    template_name = "cardsdetail/form.html"
    success_url ='/landing/success'
    fields ="__all__"

def success(request):
    return render(request, "cardsdetail/success.html")






















# def home_page(request):


# def post(request):



# def detail_page(request, card_id):
#     for c in cards_data:
#         if c['id'] == int(card_id):
#             card = c
#     return render(request, 'cardsdetail/detail.html', {'card': card})