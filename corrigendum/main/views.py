from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Corrigendum, Book


# Create your views here.
def index(request):
    book_list = Book.objects.all()
    return render(request, 'index.html', {'book_list': book_list})


def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'detail.html', {'book': book})


def edit_form(request, pk):
    c = get_object_or_404(Corrigendum, pk=pk)
    return render(request, 'edit.html', {'corrigendum': c})


def save(request):
    c = Corrigendum(text=request.POST['text'])
    book_id = request.POST['book_id']
    c.book = Book.objects.get(pk=book_id)
    c.save()
    return HttpResponseRedirect(reverse('detail', args=(book_id,)))


def add_book_form(request):
    return render(request, 'add_book.html')


def add_book(request):
    c = Corrigendum(title=request.POST['title'], text=request.POST['text'])
    c.save()
    return HttpResponseRedirect(reverse('detail', args=(c.id,)))


def history(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'history.html', {'book': book})


def search(request):
	book_list = Book.objects.filter(title__contains=request.GET['kw'])
	return render(request, 'index.html', {'book_list': book_list})
