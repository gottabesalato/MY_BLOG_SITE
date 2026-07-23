from flask_mailman import EmailMessage
from flask import render_template
from app import app

# from app import mail

def send_email(subject, sender, recipients, text_body, html_body):
    msg = EmailMessage(
        subject=subject,
        from_email=sender,
        to=recipients
        )
    msg.body = text_body
    msg.html = html_body
    msg.send()

### Send password reset email function.
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your password',
                sender=app.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
                html_body=render_template('email/reset_password.html',
                                          user=user, token=token))