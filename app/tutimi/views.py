from datetime import date
from django.shortcuts import render

def home(request, lang='en'):
    START_YEAR = 2012
    years_experience = date.today().year - START_YEAR

    context = {
        'lang': lang,
        'years_experience': years_experience,
    }
    return render(request, 'tutimi/home.html', context)

def case_studies(request):
    return render(request, 'tutimi/case_studies.html')