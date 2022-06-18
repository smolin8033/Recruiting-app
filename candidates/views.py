from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .forms import LoginForm, SignupForm
from .models import Candidate, Tag, Value


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            candidate = Candidate.objects.create(
                user=user,
                first_name=user.first_name,
                second_name=user.last_name,
            )
            login(request, user)
            return redirect('candidate', pk=candidate.id)
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


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


def tag_create(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    values_queryset = Value.objects.all()
    if request.method == 'POST':
        tag = request.POST.get('new_tag')
        values = request.POST.getlist('add_values')
        tag_object = Tag(name=tag)
        tag_object.save()

        for value in values:
            value = get_object_or_404(Value, name=value)
            tag_object.values.add(value)

        if request.POST.get('new_value'):
            new_value = request.POST.get('new_value')
            new_value = Value.objects.create(name=new_value)
            tag_object.values.add(new_value)

        candidate.tags.add(tag_object)
        return redirect('candidate', pk=pk)
    context = {
        'values_queryset': values_queryset,
        'candidate': candidate,
    }
    return render(request, 'add_tag.html', context)


def tag_delete(request, pk, candidate_id):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('candidate', pk=candidate_id)
    context = {
        'tag': tag,
        'candidate_id': candidate_id,
    }
    return render(request, 'delete_tag.html', context)
