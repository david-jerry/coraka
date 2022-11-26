import datetime
import random
import string

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject

User = get_user_model()
dt = datetime.datetime.now()

from coraka.users.models import Consent, Career, Porttfolio

def context_settings(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')




    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
        'year': dt.year,
        'ip': ip,
        'consent': True if Consent.objects.filter(ipAddress=str(ip)).exists() else False,
        'careers': Career.objects.filter(active=True),
        'portfolios': Porttfolio.objects.all(),
        # 'infura': settings.INFURA_URL + settings.INFURA_ID,
        'secs' : int(random.randint(5, 25)),
        # "APPLICATION_SERVER_KEY": settings.PUSH_NOTIFICATIONS_SETTINGS['APP_SERVER_KEY'],
        "settings": settings,
        # 'site': SimpleLazyObject(lambda: get_current_site(request)) if settings.PRODUCTION else "localhost:8000",
    }
