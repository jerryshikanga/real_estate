from django.urls import path
from . import views

app_name = 'contact'

urlpatterns =[
    path('index.html/', views.contact_page, name='contact_page'),

    path('question/list.html', views.QuestionListView.as_view(), name='question_list'),
    path('question/new.html', views.NewQuestionView.as_view(), name='question_create'),
    path('question/new/success.html', views.success_question_create, name='success_question_create'),

    path('tag/list/html', views.TagListView.as_view(), name='tag_list'),
    path('tag/new.html', views.NewQuetionTagView.as_view(), name='tag_create'),
    path('tag/new/success.html', views.success_tag_create, name='success_tag_new'),
]