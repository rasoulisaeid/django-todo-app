from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from .models import Task
from accounts.models import Profile
from django.shortcuts import redirect
import json
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def home(request):
    return render(request,'home.html')
    
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    # "-" is for descending
    ordering = "-created_at"
    context_object_name = 'tasks'
    paginate_by = 7

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:list")
    
    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'    


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:list")
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def post(self, request, *args, **kwargs):
        if is_ajax(request):
            task = self.get_object()
            data = json.loads(request.body)
            task.title = data.get("title", task.title) 
            task.status = data.get("status", task.status)
            task.save()
            return JsonResponse({'message': 'Task title updated successfully'})
    
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:list")
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return redirect(self.success_url)

