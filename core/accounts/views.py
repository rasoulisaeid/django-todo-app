from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import login 
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib import messages

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'  # Template for the login view
    fields = '__all__'  # Use all fields from the form
    redirect_authenticated_user = True  # Redirect if user is already authenticated
    
    def get_success_url(self):
        return reverse_lazy('tasks:list')  # Redirect to tasks list on successful login
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))  # Render form with errors if invalid

class RegisterView(FormView):
    template_name = 'accounts/register.html'  # Template for the registration view
    form_class = RegisterForm  # Form class for registration
    redirect_authenticated_user = True  # Redirect if user is already authenticated
    success_url = reverse_lazy('tasks:list')  # Redirect to tasks list on successful registration
    
    def form_valid(self, form):
        user = form.save()  # Save the form and create a new user
        if user:
            login(self.request, user)  # Log in the user
        return super(RegisterView, self).form_valid(form)  # Call the parent class's form_valid method
