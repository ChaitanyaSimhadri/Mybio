from django.shortcuts import render
import os
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from .forms import sms_window


model_path = os.path.join(os.path.dirname(__file__), 'artifacts', 'spam_model.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), 'artifacts', 'vectorizer.pkl')

with open(model_path, 'rb') as file1:
        model  = pickle.load(file1)

with open(vectorizer_path, 'rb') as file2:
        tfidf  = pickle.load(file2)

ps = PorterStemmer()


#text Preprocessing
def text_preprocessor(text):
    # Convert to lower case
    text = text.lower()
    
    #Removing special characters
    pattern = r'[^a-zA-Z0-9\s]'
    text = re.sub(pattern, '', text)
    
    #Tokenization
    text = nltk.word_tokenize(text)
    
    #Removing stopwords and punctualtion
    stop_words = set(stopwords.words('english'))
    text = [word for word in text if word.lower() not in stop_words]
    #Stemming
    text= [ps.stem(word) for word in text]
    
    
    return " ".join(text)


def classify_sms(message):
       transformed_sms = text_preprocessor(message)
       vector_input = tfidf.transform([transformed_sms])
       result  = model.predict(vector_input)[0]   
        
       return result

# Create your views here.
def sms_spam(request):
    submitted = False
    form = sms_window(request.POST)
    y_pred = -1
    

    if request.method =='POST':
           form = sms_window(request.POST)
           if form.is_valid:
                  message = request.POST.get('Message')
                  y_pred = classify_sms(message)

                  if y_pred == 0:
                         
                         y_pred = 'NOT SPAM'
                  elif y_pred == -1:
                          y_pred = 'Please enter Something in the text box and press Predict'
             
                  else:
                                                
                         y_pred = 'SPAM'

                                          
                

                  return render(request, 'sms.html',{'form': form, 'submitted': True, 'y_pred': y_pred})
           else:
                  form = sms_window(request.POST)
                  if 'submitted' in request.GET:
                         submitted=True

    if y_pred == 0:
                         y_pred = 'NOT SPAM'
    elif y_pred == -1:
                          y_pred = 'Please enter Something in the text box and press Predict'
             
    else:
                         
                         y_pred = 'SPAM'
           
    return render(request, 'sms.html',{'form': form, 'submitted': True, 'y_pred': y_pred})

