from django.shortcuts import render

# Create your views here.


def index(request):

    # context = {'lang': lang, 'right_data': right_data, 'text2': text2}
    return render(request, 'homepage/index.html', {})