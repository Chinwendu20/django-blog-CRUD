from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

class BlogListView(ListView):
    model=Post 
    template_name ='home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name = 'post_detail.html' 
    

class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title', 'author', 'body']
    

class BlogUpdateView(UpdateView):   
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    

class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
    
class BlogCommentView(LoginRequiredMixin,CreateView):
  model=Comment
  template_name='post_comment.html'
  form_class = CommentForm

  def get_initial(self):
    initial = super().get_initial()
    initial['name'] = self.request.user
    return initial

  def form_valid(self, form):
    form.instance.name = self.request.user
    form.instance.post_id = self.kwargs['pk']
    return super().form_valid(form)

  def get_success_url(self):
      return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

  

    
  
  
