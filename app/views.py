from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def inicio(request):
    return render(request, 'front/inicio.html')


def proceso(request):
    if request.method == "POST":

        send_mail(
            'Asunto del correo',
            'Este es el cuerpo del correo.',
            'noreply@gmail.com',
            ['ogaip87@gmail.com'],
            fail_silently=False,
        )
            
        asunto = "Asunto del correo"
        mensaje = "Este es el cuerpo del correo que deseas enviar."
        
        destinatarios = ['ogaip87@gmail.com', 'destinatario2@example.com']  # Lista de destinatarios

        try:
            send_mail(asunto, mensaje, remitente, destinatarios)
            print("Correo enviado con éxito")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
        
        return render(request, 'front/proceso.html', {
            'mensaje': 'Formulario enviado con éxito'
        })
    else:
        return render(request, 'front/proceso.html', {
            'mensaje': 'No se ha enviado el formulario'
        })
    