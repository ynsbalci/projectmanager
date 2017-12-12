from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Project
from vote.models import Vote
from .forms import ProjectCreateForm, ProjectUpdateForm, ProjectVoteForm, ProjectTaskForm
from django.contrib import messages


# Create your views here.
def active_project_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    project_list = Project.objects.filter(p_status=1)
    return render(request, 'project/index.html', {'project_list': project_list})


def confirm_project_view(request):
    if not request.user.is_authenticated():
        return redirect('home')

    project_list = Project.objects.filter(p_status=0)
    return render(request, 'project/confirm.html', {'project_list': project_list})


def project_create(request):
    if not request.user.is_authenticated():
        return redirect('home')

    form = ProjectCreateForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.p_manager = request.user
        project.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(project.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "project/create.html", context)


def project_detail(request, p_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    project = get_object_or_404(Project, p_slug=p_slug)
    context = {
        'project': project,
    }
    return render(request, "project/detail.html", context)


def project_update(request, p_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    project = get_object_or_404(Project, p_slug=p_slug)
    form = ProjectUpdateForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(project.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "project/update.html", context)


def project_vote(request, p_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    project = get_object_or_404(Project, p_slug=p_slug)
    vote = Vote.objects.filter(v_voter=request.user, v_project=project)

    form = ProjectVoteForm(request.POST or None)
    if form.is_valid():
        vote = form.save(commit=False)
        vote.v_project = project
        vote.v_voter = request.user
        # print(vote.v_voter)
        # print(vote.v_project)
        # print(vote.v_vote)
        vote.save()

        messages.success(request, "Başarılı bir şekilde oyladınız.")
        return HttpResponseRedirect(project.get_vote_url())

    context = {
        'project': project,
        'vote': vote,
        'form': form
    }

    return render(request, "project/vote.html", context)


def project_task(request, p_slug):
    if not request.user.is_authenticated():
        return redirect('home')

    project = get_object_or_404(Project, p_slug=p_slug)

    form = ProjectTaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.t_project = project
        task.save()

        messages.success(request, "Başarılı bir şekilde oyladınız.")
        return HttpResponseRedirect(project.get_task_url())

    context = {
        'project': project,
        'form': form
    }

    return render(request, "project/task.html", context)


