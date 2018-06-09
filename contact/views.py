from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import QuestionTag, Question
from django.urls import reverse_lazy


# Create your views here.
def contact_page(request, *args, **kwargs):
    return render(request, 'contact/contact.html')


class NewQuestionView(CreateView):
    model = Question
    fields = ('name', 'email', 'message', 'subject')
    success_url = reverse_lazy('contact:contact_page')


class NewQuetionTagView(CreateView):
    model = QuestionTag


class QuestionListView(ListView):
    model = Question
    paginate_by = 10
    queryset = Question.objects.all()


class TagListView(ListView):
    model = QuestionTag
    queryset = QuestionTag.objects.all()
    paginate_by = 10


def success_question_create(request, *args, **kwargs) :
    return render(request, )


def success_tag_create(request, *args, **kwargs):
    return render(request, )