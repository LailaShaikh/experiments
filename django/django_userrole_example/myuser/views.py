from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import MyUser, Role
from .decorators import roles_required

@login_required
@roles_required('editor', 'admin')
def home(request):
    return render(request, 'home.html')
