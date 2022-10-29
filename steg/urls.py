from django.urls import path, include
from . import views
from django.views.generic import RedirectView
from steg.views import Upload, ProcessImage, SelectChoice

app_name = 'steg'

urlpatterns = [
    path('', RedirectView.as_view(url='core/', permanent=True)),
    path('core/', include('core.urls')),
    path("upload/", Upload.as_view(), name='upload'),
    path("select_choice/", SelectChoice.as_view(), name="select-choice"),
    path("process/<int:choice>/", ProcessImage.as_view(), name="process"),
]