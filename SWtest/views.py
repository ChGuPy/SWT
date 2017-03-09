from django.shortcuts import render
from models import Answ, Quest
from django.http import HttpResponse
from django.forms.models import model_to_dict


# Create your views here.



def index(request):
    questions = Quest.objects.all()
    return render(request, 'index.html', {'questions': questions})


def send_answer(request):
    if request.method == 'GET':
        mes = ''
        answer = request.GET['a']
        try:
            user_answer = Answ.objects.get(id=int(answer))
            if user_answer.true_or_false:
                mes += 'Right'
        except:
           pass
    return HttpResponse(mes)

