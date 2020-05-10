from django.conf import settings # import the settings file

def admin_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    resources = {
        'EMPTY_EVENT_IMAGE': settings.EMPTY_EVENT_IMAGE,
    }
    return resources