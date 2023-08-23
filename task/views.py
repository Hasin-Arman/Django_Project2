from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from task.models import TaskModel
from task.forms import Task_Form
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

# def add_tasks(request):
#     return render(request, 'add_task.html')

class Add_Book_view(CreateView):
    model=TaskModel
    form_class=Task_Form
    template_name='add_task.html'
    success_url=reverse_lazy('showpage')
    
class show_book_view(ListView):
    model=TaskModel
    template_name='show_task.html'
    context_object_name='tasks'

class edit_book_view(UpdateView):
    model=TaskModel
    form_class=Task_Form
    template_name='add_task.html'
    success_url=reverse_lazy('showpage')

class del_book_view(DeleteView):
    model=TaskModel
    template_name='del_conf.html'
    success_url=reverse_lazy('showpage')

class complete_task_view(DetailView):
    model=TaskModel
    template_name='completed_tasks.html'
    context_object_name='data'
    pk_url_kwarg='id'
    
    
    