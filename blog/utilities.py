from .models import *
from django.contrib.auth.models import User
def authenticate(username, password):
    try:
        blgUser = blogUser.objects.get(username=username)
        if blgUser.password == password:
            return True
    except:
        Userobj = User.objects.get(username=username)
        if Userobj:
            return True    
    else:
        return False