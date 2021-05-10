from django.shortcuts import render
from .models import New, Press, Contact, Portfolio

# Create your views here.


def index(request):
    news = New.objects.all()
    presss = Press.objects.all()
    Portfolios = Portfolio.objects.all()

    return render(request, 'index.html', {'news': news, 'presss': presss, 'portfolios': Portfolios})


def introduction(request, section):
    print(section)
    return render(request, 'introduction/introduction.html')


def businessArea(request, section):
    print(section)
    return render(request, f'businessArea/{section}.html')


def portfolio(request, section):
    print(section)
    return render(request, f'portfolio/{section}.html')


def community(request, section):
    print(section)
    return render(request, f'community/{section}.html')


def recruiting(request, section):
    print(section)
    return render(request, f'recruiting/{section}.html')
