from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from . import models, forms
from .models import Book


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = "book.html"
    context_object_name = "book"


class CreateBlogView(CreateView):
    model = Book
    template_name = "book.html"
    fields = [
        "image",
        "title",
        "description",
    ]


class BookCreateView(CreateView):
    template_name = 'book_create.html'
    form_class = forms.BookForm
    success_url = '/'
    queryset = models.Book.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)


class BookDetailView(DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=id_)


class BookUpdateView(UpdateView):
    template_name = 'book_create.html'
    form_class = forms.BookForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book:book-list')


class BookDeleteView(DeleteView):
    template_name = 'book_delete.html'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=id_)

    def get_success_url(self):
        return reverse('book:book-list')
