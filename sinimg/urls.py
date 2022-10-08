from django.urls import path
from sinimg.views import ImgToPdf
app_name = 'sinimg'

urlpatterns = [
    path("imgtopdf/", ImgToPdf.as_view(), name='img-to-pdf'),
]