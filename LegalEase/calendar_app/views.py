from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event
from django.urls import reverse_lazy

class EventListView(ListView):
    model = Event
    template_name = 'calendar_app/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'calendar_app/event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    template_name = 'calendar_app/event_form.html'
    fields = ['title', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'calendar_app/event_form.html'
    fields = ['title', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'calendar_app/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')
