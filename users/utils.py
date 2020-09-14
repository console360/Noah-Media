from noah.send_email import send_email_ses
from django.template.loader import get_template
from noah import settings


def send_forgot_password_email(user, password):

    html_template = get_template('forgot_password.html')
    html_content = html_template.render({'name': user.name, 'new_password': password})
    ok, message_id = send_email_ses(settings.EMAIL_SENDER_ID, [user.email],
                                    "Did you forget your password? Don't worry. We're here to help you.",
                                    body=html_content)

    return ok, message_id
