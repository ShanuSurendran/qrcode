
from django.shortcuts import render
import pyqrcode
from PIL import ImageTk,Image
import cv2

# Create your views here.
data=None

def generate(request):
    global data
    if request.method == 'POST':
        data = request.POST['data']
        if data==None:
            return render(request,'index.html')
        else:

            file_name = r'C:\Users\SHANU\Rapidapi_1\qrcodeproject\qrcodeproject\static\images\test.png'
            url = pyqrcode.create(data)
            url.png(file_name, scale=8)
            img= Image.open(file_name)
            return render(request,'index.html', {'img': img})


    else:
        pass

    return render(request, 'index.html')


def save(request,):
    image=cv2.imread(r'C:\Users\SHANU\Rapidapi_1\qrcodeproject\qrcodeproject\static\images\test.png',1)
    cv2.imwrite("QRCode.png",image)
    return render(request,'index.html')





