from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Lead, Agent
from .forms import LeadForm, CustomUserCreationForm

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(ListView):
    template_name = "leads/list_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        send_mail(
            subject='A lead has been created',
            message='Go to the main page to see the new lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm
    def get_success_url(self):
        return reverse("leads:lead-list")

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")