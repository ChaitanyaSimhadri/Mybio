from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
import pickle
from .forms import predict_form,Contact_form
import numpy as np
from django.http import FileResponse
from django.views import View
from django.contrib import messages
import json
import os

from django.core.mail import send_mail

# import pandas as pd, numpy as np

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression,Lasso, Ridge
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import make_pipeline
# from sklearn.metrics import r2_score



# Create your views here.

def home(request):
    return render(request, 'home.html',{})


model_path1 = os.path.join(os.path.dirname(__file__), 'artifacts', 'columns.json')
model_path2 = os.path.join(os.path.dirname(__file__), 'artifacts', 'model3.pickle')


with open(model_path1, 'r') as file1:
        columns = json.load(file1)['data_columns']
        locations = columns[3:]
with open(model_path2, 'rb') as file2:
        model  = pickle.load(file2)



def get_estimated_price(location,BHK,total_sqft,bath):
       
       try:
                        loc_index = locations.index(location.lower())
                            
       except:
                            
                            loc_index = -1
       x = np.zeros(len(columns))
       x[0] = int(BHK)
       x[1] = float(total_sqft)
       x[2] = int(bath)
       
       if loc_index>=0:
        
        x[loc_index+1] =1
        
        
       return round(model.predict([x])[0],2)


          
       
        

def predict(request):
       submitted = False
       y_pred = 0
       
       

       if request.method == 'POST':
              form =  predict_form(request.POST)
              if form.is_valid():
                     
                     location = request.POST.get('Location')
                     BHK = request.POST.get('Bedrooms')
                     total_sqft = request.POST.get('SQFT')
                     bath = request.POST.get('BathRoom')
                     
                     y_pred = get_estimated_price(location, BHK, total_sqft, bath)

                     
                     return render(request, 'Predict.html', {'form': form, 'submitted': True, 'y_pred': y_pred,'location':location,'BHK':BHK,'total_sqft':total_sqft})
       else:
              
              form =  predict_form(request.POST)
              if 'submitted' in request.GET:
                     
                     submitted = True 
              
                  
       
       return render(request, 'Predict.html',{'form':form, 'submitted':submitted,'y_pred':y_pred,'locations':locations})



def contact(request):
       if request.method =="POST":
              name = request.POST['name']
              email = request.POST['email']
              phone = request.POST['phone']
              to_email = 'chaitanyasimhadrii@gmail.com'
              message = request.POST['message']
              
              send_mail(name,message+ ''+phone+''+email,to_email,['hnagacha@gmail.com'],)
                     
                     
                     
                     
              return render(request, 'contact.html',{'name':name})
       else:

       
        return render(request, 'contact.html',{})
 


class DownloadFileView(View):
    def get(self, request, file_name):
        file_path = os.path.join(os.path.dirname(__file__), 'artifacts', 'NagaChaitanya_Resume.pdf')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = FileResponse(file)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response
        else:
            return HttpResponse("File not found", status=404)





