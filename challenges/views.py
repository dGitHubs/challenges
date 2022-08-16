from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    'december': None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html", {
        "months": months,
    })


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
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        raise Http404()
