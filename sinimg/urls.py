from django.urls import path
from sinimg.views import Upload, ProcessImage, SelectChoice

app_name = 'sinimg'

urlpatterns = [
    path("upload/", Upload.as_view(), name='upload'),
    path("select_choice/", SelectChoice.as_view(), name="select-choice"),
    path("process/<int:choice>/", ProcessImage.as_view(), name="process"),
]