from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from sinimg.forms import SinImgForm
from sinimg.helper import color_to_bw, img_to_pdf, blur
# Create your views here.

class ImgToPdf(View):
    def get(self, request):
        form = SinImgForm()
        context = {
            "form": form,
        }
        return render(request, "sinimg/img_to_pdf.html", context)
    
    def post(self, request):
        form = SinImgForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            # print(form.cleaned_data["img"])
            img = obj.img
            # print(img.read())
            # buf = img_to_pdf(img)
            gray = color_to_bw(img.path)
            blured = blur(img.path)
            return FileResponse(blured, as_attachment=True, filename="demo.png")
        context = {
            "form": form,
        }
        return render(request, "sinimg/img_to_pdf.html", context)
