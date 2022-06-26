from django.shortcuts import render
import random
# Create your views here.

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generater_password =''

    lenght = int(request.GET.get('length'))

    if request.GET.get('uppercase'):    #si uppercase true -> agrega mayusculas a la lista
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('*-/-_~%$#"&()'))

    if request.GET.get('numers'):
        characters.extend(list('0123456789'))

    for x in range(lenght):
        generater_password += random.choice(characters)

    return render(request, 'generator/password.html',{'password':generater_password})
