import cv2
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from .testing import *


def login_view(request):
    # capture = cv2.VideoCapture(0)
    if request.method == 'POST':
        capture = cv2.VideoCapture(0)

        if not capture.isOpened():
            return 'Error: Unable to access the camera'

        ret, frame = capture.read()
        capture.release()
        
        cv2.imwrite('captured_image.jpg', frame)
        # import pdb;
        # pdb.set_trace()
        user_data = tester()
        context= {"data":user_data}
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')