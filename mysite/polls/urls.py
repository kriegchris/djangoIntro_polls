from django.urls import path
from . import views

app_name="polls"

urlpatterns = [
    path('', views.index, name='index'),

    # 127.0.0.1/polls/[id#]/
    path('<int:question_id>/', views.detail, name='detail'),
    # 127.0.0.1/polls/[id#]/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # 127.0.0.1/polls/[id#]/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
