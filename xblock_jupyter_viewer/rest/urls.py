"""
Defines a URL to return a notebook html page to be used in an iframe
"""
# from django.conf.urls import url
from django.urls import path
from .views import NotebookViewer

app_name = 'xblock_jupyter_viewer'

urlpatterns = [
    path(
    'render_notebook/',
        NotebookViewer.as_view(),
        name='jupyter_nb_viewer'
    )
]



