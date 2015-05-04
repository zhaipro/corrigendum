from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Corrigendum


# Create your views here.
def index(request):
    corrigendum_list = Corrigendum.objects.all()
    return render(request, 'index.html', {'corrigendum_list': corrigendum_list})


def detail(request, pk):
    c = get_object_or_404(Corrigendum, pk=pk)
    return render(request, 'detail.html', {'corrigendum': c})


def edit_form(request, pk):
    c = get_object_or_404(Corrigendum, pk=pk)
    return render(request, 'edit.html', {'corrigendum': c})


def save(request):
    c = Corrigendum(pk=request.POST['pk'], title=request.POST['title'], text=request.POST['text'])
    c.save()
    return HttpResponseRedirect(reverse('detail', args=(c.id,)))


def add_form(request):
    return render(request, 'add_form.html')


def add(request):
    c = Corrigendum(title=request.POST['title'], text=request.POST['text'])
    c.save()
    return HttpResponseRedirect(reverse('detail', args=(c.id,)))
