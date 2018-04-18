# -*- encoding: utf-8 -*-

#-- Funciones genericas para el proyecto
from django.contrib.sessions.models import Session
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

#--- Settings base
from intineratour.settings import base
#-- Send Mail
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.header import Header
import smtplib
import json

# from django.contrib.auth.models import User

from accounts.models import User

#import que se utiliza para generar un string
#aleatorio de caracteres, para getsynckey
from django.utils.crypto import get_random_string

#-- Hash
import hashlib, datetime, random

from accounts.models import UserRequest
import utilies as ut


#-- Funcion para Obtener el ID del usuario que tiene la sesion iniciada
#-- Recibe un objeto de tipo "request" y devuelve el ID del usuario. Ej: user_id = get_user_id(request)
def get_user_id(request):
    s = Session.objects.get(pk=request.session.session_key)
    #-- Obtenemos el id del usuario que se esta logueado
    uid = s.get_decoded().get('_auth_user_id')

    return uid

#-- función para obtener la ip del cliente
def get_ip_user(request):
    x_forward_for = request.META.get('HTTP_X_FORWARD_FOR')
    ip = None
    if(x_forward_for):
        ip = x_forward_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


#-- Funcion para el envio de correos con Send_mail
#-- Recibe 3 parametros: subject=asunto, body=cuerpo del mensaje, emails=Lista de correos a los que se les enviara el mail
#-- Ej: sendmail('tu asunto','cuerpo del mensaje','[hugo@sml.mx, info@sml.mx]')
def sendmail(subject, body, emails):
    #-- Sendmail: (Subjetc, body, email host, email user, False)
    send_mail(subject, body, base.EMAIL_HOST_USER ,[emails], fail_silently=False)

#-- funcion que guarda/sube una imagen al servidor
#-- OJO esta ya tiene una parte del path
#-- regresa true si se guarda la imagen y false si no
#-- ejemplo: save_file( request['file'], 'img/' )
def save_file(file, path=''):
    ''' Little helper to save a file '''
    try:
        filename = file._get_name()
        fd = open('%s/%s' % ( settings.MEDIA_ROOT , str(path) + str(filename)), 'wb')
        for chunk in file.chunks():
            fd.write(chunk)
        fd.close()
        return True
    except Exception:
        return False;
#-- Funcion para crear las llaves de activacion en las vistas donde se ocupe enviar correo
#-- Recibe 3 parametros: email=Correo al que se enviará, usermodel=Modelo del User para obtener el id y guardarlo en tabla de Request, typeact=Tipo de solicitud : 1 - Correo de Activacion de la cuenta, 2 - Correo de Recuperar contraseña )
#-- No regresa nada
#-- ejemplo: sendmail_activacions('info@sml.mx', usermodel, )
def sendmail_activations(email, usermodel, typeact):
    #-- Creamos las llaves del envio de correo
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    activation_key = hashlib.sha1(salt+email).hexdigest()
    expires_key = datetime.datetime.today() + datetime.timedelta(2)

    #-- Guardamos las llaves de activacion
    user_request = UserRequest.objects.create(
        user = usermodel,
        activation_key=activation_key,
        expires_key=expires_key,
        activation_type=typeact,
        activation_status=0
    )

    # Enviar correo con llave de activacion
    if(typeact == '1'):
        email_subject = 'Itineratur : Activacion de su Cuenta'
        email_body = "Bienvenido a su nueva cuenta de Itineratur, la herramienta de confianza del agricultor. \
         El primer paso es activar su cuenta dando click en el siguiente enlace que expirara dentro de 48 horas. \
        https://itineratur.com/recovery/users/activation/%s" % (activation_key)
    elif (typeact == '2'):
        email_subject = 'Itineratur : Recuperacion de Contraseña'
        email_body = "Estimado usuario.\n Se ha solicitado la recuperacion de contrasena de su cuenta Itineratur.\
        Para continuar con el proceso haga click en el siguiente enlace que expirara dentro de 48 horas. \
        https://itineratur.com/recovery/users/recoverypassword/%s . \n Si usted no ha iniciado solo ignore este mensaje." % (activation_key)

    #-- Sendmail: (Subject, body, email user)
    sendmail(email_subject, email_body, email)


    #funcion que regresa el sync key de un registro
     # recien creado, este campo sirve para verificar la
     # sincronizacion entre la plataforma web y la app movil,
     # se compone del:
     # nombre del custoner ( customer_name )
     # email del usuario ( user_email )
     # la fecha con minutos y segundos ( timestam )
     # y una cadena de 12 caracteres aleatorios ( 12 random char )
     #NOTA: es sumamente importante que se utilice esta funcion al
     #crear un regitro

def send_email(from_, to_, subj_msg, body_msg):
    try:
        msg = MIMEMultipart()
        msg['From'] = from_
        msg['To'] = to_
        msg['Subject'] = Header(subj_msg, 'utf-8')

        msg.attach(MIMEText(body_msg, 'plain', 'utf-8'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_, 'Gordopanela')
        text = msg.as_string()
        server.sendmail(from_, to_, text)
        server.quit()
    except Exception as e:
        print e

def pagination(instance, page, num):
    paginator = Paginator(instance, num)

    try:
        obj_list = paginator.page(page)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_page)

    return obj_list
