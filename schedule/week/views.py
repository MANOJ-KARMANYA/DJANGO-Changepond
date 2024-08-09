from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

week_schedule = {
    'monday': 'Learning Python',
    'tuesday': 'Learning .Net',
    'wednesday': 'Learning Adv Python',
    'thusday': 'Learning Angular',
    'friday': 'Learning React',
    'saturday': 'Learning jest',
    'sunday': 'Learning Git',
}


def week_details_by_number(request, week):

    weeks = list(week_schedule.keys())   

    if(week>len(weeks)):
        return HttpResponseNotFound('Invalid Month')
   
    redirect_week = weeks[week-1]
    redirect_path = reverse('week-details', args=[redirect_week])

    return HttpResponseRedirect(redirect_path)

def week_details(request, week):
    try:
        week_text = week_schedule[week]
        return HttpResponse(week_text)
    except:
        return HttpResponseNotFound('This is not mentioned')