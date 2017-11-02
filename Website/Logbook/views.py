from django.views import generic
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Log, Entry
import datetime
from django.db.models import Q

class IndexView(generic.ListView):
    template_name = 'Logbook/index.html'
    context_object_name = 'all_logs'

    def get_queryset(self):
        return Log.objects.all()

# Create your views here.
