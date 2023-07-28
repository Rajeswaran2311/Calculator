from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . models import Todo_entry
from django.views.decorators.csrf import csrf_exempt
def cal(request):
    return render(request,'calc.html')
def todo(request):
    todo=Todo_entry.objects.all()
    template=loader.get_template('todo.html')
    context={
        'todo':todo,
    }
    return HttpResponse(template.render(context,request))
def add(request):
        entry=request.POST['entry']
        member=Todo_entry(entry=entry)
        member.save()
        return HttpResponseRedirect(reverse('todo'))
def delete(request,id=None):
        if id!=None:
            member = Todo_entry.objects.get(id=id)
            member.delete()
        else:
            Todo_entry.objects.all().delete()
        return HttpResponseRedirect(reverse('todo'))


