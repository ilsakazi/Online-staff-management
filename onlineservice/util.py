import uuid

from django.utils.text import slugify

def generateslug(title:str):
    from .models import Faculty
    title=slugify(title)
    while(Faculty.objects.filter(slug=title).exists()):
        title= f'{slugify(title)}-{str(uuid.uuid4())[:4]}'

    return title