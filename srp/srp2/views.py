from django.shortcuts import render
import os
from django.contrib import messages
from .forms import ImageForm
from django.views.generic import TemplateView
# Create your views here.

import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

class predictImage(TemplateView):
    
    form = ImageForm
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance
            print(img_object.LeafName)
            imgPath = img_object.userImg.url
            imgPath = imgPath.split('/')[4]
            file_path = os.path.join('D:/Semesters/semester6/SRP-2/Leaf-Disease-Detection-Cure-ML/srp/srp2/media/upload', imgPath)
            
            test_image = load_img(file_path, target_size = (256, 256,3)) # load image 
            test_image = img_to_array(test_image)/255 # convert image to np array and normalize
            test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D

            file_path = os.path.join('D:/Semesters/semester6/SRP-2/Leaf-Disease-Detection-Cure-ML/models', img_object.LeafName)
            print(file_path)
            model = load_model(file_path)
            
            result = model.predict(test_image) # predict diseased palnt or not
            pred = np.argmax(result, axis=1)
          
            df = pd.read_csv("D:/Semesters/semester6/SRP-2/Leaf-Disease-Detection-Cure-ML/srp/static/supplement_info.csv", encoding = "ISO-8859-1", engine='python')
            row = df.iloc[2, :]
            
            steps = row[6].split('.')
            
            cure = {'disease_name' : row[1],
                    'supplement_name' : row[2],
                    'supplement_img' : row[3],
                    'buy_link' : row[4],
                    'description' : row[5],
                    'steps' : steps,
                    'disease_img' : row[7],
                    'img_obj':img_object
                    }
            return render(request,'result.html',cure) 
                 
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
