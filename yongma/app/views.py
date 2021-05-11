from django.shortcuts import render
from .models import New, Press, Contact, Portfolio

# Create your views here.


def index(request):
    news = New.objects.all()
    presss = Press.objects.all()
    Portfolios = Portfolio.objects.all()

    return render(request, 'index.html', {'news': news, 'presss': presss, 'portfolios': Portfolios})


def section(request, category, section):
    print(category, section)
    data = {}

    # 뉴스룸
    if (category == 'community') and (section == 'newsRoom'):
        news = New.objects.all()
        data = {'news': news}

    # 프레스
    if (category == 'community') and (section == 'press'):
        presss = Press.objects.all()
        data = {'presss': presss}

    if (category == 'community') and (section == 'contact'):
        if request.method == 'POST':
            Contact.objects.create(
                category=request.POST['category'],
                client_name=request.POST['client_name'],
                client_email=request.POST['client_email'],
                client_number=request.POST['client_number'],
                title=request.POST['title'],
                contents=request.POST['contents']
            )

    return render(request, f'{category}/{section}.html', data)


def post_view(request, category, section, post_pk):
    if (category == 'community') and (section == "newsRoom"):
        post = New.objects.get(pk=post_pk)
        return render(request, f'{category}/news.html', {'post': post})
