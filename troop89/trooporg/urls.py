from django.urls import path

from . import views

MONTH_FORMAT = '%m'

app_name = 'trooporg'

urlpatterns = [
    path(
        '',
        views.CurrentTermDetailView.as_view(),
        name='current-term',
    ),
    path(
        '<int:year>/<int:month>/<int:day>/',
        views.TermDetailView.as_view(month_format=MONTH_FORMAT),
        name='term-detail',
    ),
    path(
        'terms/',
        views.TermListView.as_view(),
        name='term-list'
    ),
    path(
        'patrols/<slug:slug>/',
        views.PatrolDetailView.as_view(),
        name='patrol-detail',
    ),
]
