from django.shortcuts import render
from .models import addtodoItem
from django.http import HttpResponseRedirect

def todoAppView(request):
    all_items=addtodoItem.objects.all()
    return render(request,"todo.html",{'x':all_items})
# Create your views here.
def addtodo(request):
    new_item=addtodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def delete(request,y):
    item_to_delete=addtodoItem.objects.get(id=y)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
