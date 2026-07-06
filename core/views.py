def zayavki(request):
    # Проверка пароля через POST-запрос
    if request.method == 'POST':
        password = request.POST.get('password', '')
        
        # Обработка входа с паролем
        if password == '1583gusev':
            appointments = Appointment.objects.all().order_by('-created_at')
            return render(request, 'core/zayavki_table.html', {'appointments': appointments})
        elif password:
            return render(request, 'core/zayavki.html', {'error': 'Неверный пароль'})
        
        # Обработка изменения статуса
        toggle_id = request.POST.get('toggle_status')
        if toggle_id:
            try:
                appointment = Appointment.objects.get(id=toggle_id)
                appointment.is_processed = not appointment.is_processed
                appointment.save()
            except Appointment.DoesNotExist:
                pass
            appointments = Appointment.objects.all().order_by('-created_at')
            return render(request, 'core/zayavki_table.html', {'appointments': appointments})
        
        # Обработка удаления всех заявок
        if request.POST.get('delete_all'):
            Appointment.objects.all().delete()
            appointments = Appointment.objects.all().order_by('-created_at')
            return render(request, 'core/zayavki_table.html', {'appointments': appointments})
    
    # GET-запрос — показываем форму ввода пароля
    return render(request, 'core/zayavki.html')
