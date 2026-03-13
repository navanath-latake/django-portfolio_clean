from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project, Experience
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent! I'll get back to you soon.")
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'experiences': Experience.objects.all(),
        'form': form,
    }
    return render(request, 'portfolio_app/index.html', context)
