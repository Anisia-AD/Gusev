from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import Appointment

def index(request):
    return render(request, 'core/index.html')

def services(request):
    return render(request, 'core/services.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        problem = request.POST.get('problem', '').strip()
        agree = request.POST.get('agree')
        
        if not name or not phone or not problem:
            messages.error(request, 'Пожалуйста, заполните все поля формы.')
            return render(request, 'core/appointment.html')
        
        if not agree:
            messages.error(request, 'Необходимо согласие на обработку персональных данных.')
            return render(request, 'core/appointment.html')
        
        try:
            Appointment.objects.create(
                name=name,
                phone=phone,
                problem=problem
            )
            
            messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            return HttpResponseRedirect(reverse('index'))
            
        except Exception as e:
            messages.error(request, 'Произошла ошибка. Попробуйте позже.')
            return render(request, 'core/appointment.html')
    
    return render(request, 'core/appointment.html')

def zayavki(request):
    return HttpResponse("Страница заявок работает!")
