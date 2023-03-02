from . models import Category

def get_menu(request):
    link=Category.objects.all()
    return dict(link=link)