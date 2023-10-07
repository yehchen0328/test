from django.core.mail import send_mail, get_connection

def send_email_with_user_credentials(request):
    user_email = request.POST.get('user_email')
    user_password = request.POST.get('user_password')

    with get_connection(
        host="smtp.gmail.com",
        port=587,
        username=user_email,
        password=user_password,
        use_tls=True
    ) as connection:
        send_mail(
            'Subject here',
            'Here is the message.',
            user_email,
            ['recipient@example.com'],
            connection=connection
        )