import cv2
import numpy as np
import urllib.request
from django.contrib import messages
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from sinimg.forms import SinImgForm
from sinimg.helper import blur, color_to_grayscale, clr_to_bw, decrypt_image, encrypt_image, img_to_pdf, resize, sharp
from sinimg.models import SinImg

CHOICES = ["Convert To GrayScale", "Convert To PDF", "Convert To Blur", "Convert To Black And White", "Resize Image", "Encrypt Image", "Decrypt Image","Sharpen Image"]

class ProcessImage(View):
    '''
    A class to process an image.
    '''
    def get(self, request, choice):
        '''
        Shows the successfully processed page.
        '''
        return render(request, "sinimg/process.html")

    def post(self, request, choice):
        '''
        Returns the processed image.
        '''
        id = request.session.get("id")
        obj = SinImg.objects.get(id=id)

        # Retrieving the image and storing it in memory
        url = obj.img.url
        req = urllib.request.urlopen(url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        path = cv2.imdecode(arr, -1) # 'Load it as it is'

        content_type = "image/png"
        file_name = "demo.png"

        if choice == 0:
            img = color_to_grayscale(path)
        elif choice == 1:
            img = img_to_pdf(path)
            content_type="application/pdf"
            file_name = "demo.pdf"
        elif choice == 2:
            img = blur(path)
        elif choice == 3:
            img = clr_to_bw(path)
        elif choice == 4:
            img = resize(path)
        elif choice == 5:
            img = encrypt_image(path)
        elif choice == 6:
            img = decrypt_image(path)
        elif choice == 7:
            img = sharp(path)
        else:
            return HttpResponse("Invalid Option")

        option = request.POST.get("type")
        
        if option == "Preview":
            image_data = img.getvalue()
            return HttpResponse(image_data, content_type=content_type)
        elif option == "Download":
            return FileResponse(img, as_attachment=True, filename=file_name)
        else:
            return HttpResponse("Invalid Option")

class SelectChoice(View):
    '''
    A class to show the image processing choices.
    '''
    def get(self, request):
        '''
        Shows the image processing choice page.
        '''
        id = request.session.get("id")
        obj = SinImg.objects.get(id=id)
        context={
                "object": obj, 
                "choices": CHOICES,
                }
        return render(request, "sinimg/select_choice.html", context)

    def post(self, request):
        '''
        Returns the image processing choice.
        '''
        type = request.POST.get("type")
        if type:    
            choice_id = CHOICES.index(type)
            return redirect((reverse_lazy("sinimg:process", kwargs={"choice": choice_id})))
        else:
            return HttpResponse("Invalid Choice")

class Upload(View):
    '''
    A class to upload an image.
    '''
    def get(self, request):
        '''
        Shows the upload page.
        '''
        form = SinImgForm()
        context = {
            "form": form,
        }
        return render(request, "sinimg/upload.html", context)
    
    def post(self, request):
        '''
        Uploads the image or sends a warning if the submitted file is not an image.
        '''
        form = SinImgForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            request.session['id'] = obj.id     
            return redirect(reverse_lazy("sinimg:select-choice"))
        else:
            messages.warning(request, 'Please select a Picture')
            return HttpResponseRedirect(request.path)