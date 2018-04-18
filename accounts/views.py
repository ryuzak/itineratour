# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def users_add(request):
    if request.method == 'POST':
        #-- Campos de la forma de registro de usuario
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            validation = User.objects.filter(email__iexact=user_form.cleaned_data.get('email')).exclude(email__iexact=user_form.cleaned_data.get('email'))
            if validation :
                email_user = User.objects.get(emal=email)
                if email_user.email == email and email_user.status == '-1':
                    user_form.save(update_fields=[user_form])
                    User.objects.filter(pk=email_user.pk).update(status='1')
                    user_model = user_form.save()
                    #-- Redireccionamos a la lista de usuarios
                    return redirect('accounts:users_list')
    else:
        user_form = UserForm()
    return render(request, 'accounts/user.html', {'form' : user_form, 'header' : 'Agregar Usuario'})
