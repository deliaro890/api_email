from django.shortcuts import render

# Create your views here.

#rest_framework
from rest_framework import status, viewsets,mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

#serializers
from api_correo.serializers import api_correoSerializer


from django.core.mail import send_mail

from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives

class api_correoViewSet( mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = api_correoSerializer

    def create(self, request, *args, **kwargs):
        serializer = api_correoSerializer(data=request.data)

        if serializer.is_valid():
                
            nombre = serializer.data['nombre']
            correo = serializer.data['correo']
            asunto = serializer.data['asunto']
            mensaje = serializer.data['mensaje']

            send_ = send_correo(nombre,correo,asunto,mensaje)

            response = super(api_correoViewSet,self).create(serializer)
            data={'status':'success','data-in':response.data}
            response.data = data
            return response
        
        else:

            data = {
                'status': 'datos de entrada erroneos',
                'error': serializer.errors,
                'status_code':status.HTTP_400_BAD_REQUEST        
            }
            
            return Response(data,status=status.HTTP_400_BAD_REQUEST)

def send_correo(nombre,correo,asunto,mensaje):

    """ send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['deroman890@gmail.com'],
        fail_silently=False,
    ) """

    """ email_mess = EmailMessage(
        subject='jojo',
        body='body',
        from_email='ejemplo@example.com',
        to=['deroman890@gmail.com'

        ],
    ) """

    

    subject, from_email, to = 'Contacto Pulpo', 'from@gmail.com', 'deroman890@gmail.com'
    text_content = 'This is an important message.'
    html_content = '<p>Nombre: '+nombre+'<br> <strong>Correo: '+correo+'<br></strong>Mensaje: '+mensaje+'</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    #email_mess.content_subtype='html'
    #email_mess.send()

    return 'hola'
        


