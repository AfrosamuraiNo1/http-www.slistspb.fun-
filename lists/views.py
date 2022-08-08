from django.shortcuts import redirect,render
from lists.models import Item, List

# Создайте ваши представления здесь.
def home_page(request):
#    if request.method == 'POST':
#        Item.objects.create(text=request.POST['item_text'])
#        return redirect('/lists/trustory/')
    return render(request, 'home.html')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def view_list(request):
#'''представление списка'''
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})

def new_list(request):
#    '''новый список'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/trustory/')