from django.shortcuts import render

def about_page(request):
    return render(request, 'about.html')

def home_page(request):
    return render(request, 'home.html')

def contacts_page(request):
    return render(request, 'contacts.html')

