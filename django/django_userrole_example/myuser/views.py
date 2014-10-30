from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import MyUser, Role
from .decorators import roles_required

@login_required
@roles_required('editor', 'admin')
def home(request):
    return render(request, 'home.html')


def generate_css_file(border, font_color, background, highlight,\
                      title_color, des_color, font, filename='test.css',path=''):
    #generate css file for the given params
    wtext = ''
    if font_color:
        wtext = '''body {
                    font-family: "Helvetica Neue",Helvetica,%s,sans-serif;
                    font-size: 14px;
                    line-height: 1.42857143;
                    color: #%s;
                    background-color: #%s;
}
'''
        wtext =  wtext %(font, font_color, background)

    #write
    if wtext:
        with open(filename, 'wb') as f:
            f.write(wtext)

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