from django.shortcuts import render
from django.contrib.auth import authenticate

def login_pagina(request):
    if request.method == 'GET':
        return render (request, 'login.html')
    else: 
        authenticate(request, username = request.POST['username'], password = request.POST['password'])
        
        print(request.POST)
        
        return render(request, 'login.html')
    
    # return render(request, 'login.html')
