from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView

from .forms import LoginForm
from .models import Candidate


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                else:
                    candidate = get_object_or_404(Candidate, user=request.user)
                    return redirect('candidate', pk=candidate.id)
            else:
                return HttpResponse('Please, enter valid login and password')
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'candidate.html'


class CandidateListView(ListView):
    model = Candidate
    template_name = 'main_page.html'
