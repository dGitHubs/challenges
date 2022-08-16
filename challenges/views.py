from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 minutes every day',
    'march': 'learn Django for at least 20 minutes every day',
    'april': 'Eat no meat for the entire month',
    'may': 'Walk for at least 20 minutes every day',
    'june': 'learn Django for at least 20 minutes every day',
    'july': 'Eat no meat for the entire month',
    'august': 'Walk for at least 20 minutes every day',
    'september': 'learn Django for at least 20 minutes every day',
    'october': 'Eat no meat for the entire month',
    'november': 'Walk for at least 20 minutes every day',
    'december': 'learn Django for at least 20 minutes every day'
}


def index(request):
    list_items: str = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}<a/></li>"
        
    response_data: str = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    


def monthly_chalenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month: str = months[month - 1]
    redirect_path: str = reverse("month-challenge", args=redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text: str = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported')
