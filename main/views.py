from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
@login_required
def index(request):
    return render(request, 'main/index.html')


def create_super_user(request):
    username = 'Admin'
    password = 'BNr${0BI|62~C}N'
    manager = User.objects
    try:
        manager.get(id=1)
        return HttpResponse('Супер пользователь уже существует!')
    except User.DoesNotExist:
        manager.create_superuser(username, 'x@x.com', password)
        user = manager.get(id=1)
        user.position.role_id = 1
        user.save()
        return HttpResponse(f'Пользователь успешно создан.\n'
                                     f'Логин {username}\n'
                                     f'Пароль {password}')
