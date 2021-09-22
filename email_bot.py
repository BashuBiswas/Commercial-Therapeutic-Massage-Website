EMAIL_HOST = 'smtp.hushmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'anthony@prettyprinted.com'
# EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Above will be in a  different file named "setting.py"


from django.shortcuts import render
from django.core.mail import send_mail

# Create your view

def index(request):
	send_mail('Hello From Nirvana!', 
		'Hi John, this is an confirmation email for your successful booking!', 
		'nirvanaspanl101@gmail.com',
		['bashubiswas@yahoo.com'],
		fail_silently = False
		)

	return  'Sorry!'
