from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.conf import settings
from .models import MyUser, Role
from .decorators import roles_required

import os

@login_required
@roles_required('editor', 'admin')
def home(request):
    return render(request, 'home.html')


def generate_css_file(border, font_color, background, highlight,\
                      title_color, des_color, font, filename='test.css',path=''):
    #generate css file for the given params
    wtext = ''
    if font_color or background or title_color:
        with open(settings.BASE_DIR + '/static/template.less') as f:
            wtext = f.read()

        wtext =  wtext %(background, border, font, font_color)

        with open(settings.BASE_DIR + '/static/test.less', 'wb') as f:
            f.write(wtext)

        os.system('lessc static/test.less > static/test_out.css')


def customize_page_style(request):
    border = request.GET.get('border-color')
    font_color = request.GET.get('font-color')
    background = request.GET.get('background-color')
    highlight = request.GET.get('highlight-color')
    title_color = request.GET.get('title-color')
    des_color = request.GET.get('des-color')
    font = request.GET.get('font')

    print border, font_color, background, highlight,title_color, des_color, font

    val = request.GET
    if len(val):
        generate_css_file(border, font_color, background, highlight,\
                          title_color, des_color, font)

    return render(request, 'customize.html')