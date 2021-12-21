from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
    return HttpResponse("여기서 이게 뜨네")

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')

    elif request.method == 'POST':
        user_id = request.POST.get('id','')
        user_pw = request.POST.get('pw','')
        user_pw_confirm = request.POST.get('pw-confirm','')
        user_name = request.POST.get('name','')
        
        if (user_id or user_pw or user_pw_confirm or user_name) == '':
            return redirect('/user/register')
        elif user_pw != user_pw_confirm:
            return redirect('/user/register')
        else:
            user = User(
                user_id = user_id,
                user_pw = user_pw,
                user_name = user_name
            )
            user.save()
        return redirect('/')