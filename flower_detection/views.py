
from django.shortcuts import render, redirect
from django.http import HttpResponse



#models
from .models import Info
from .models import predict


from .forms import predictForm


# from .forms import predictForm


#tenserflow
from tensorflow.python.eager.context import context
import win32gui
from PIL import ImageGrab, Image
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
from django.contrib import messages



# #upload 
# from flower_detection.forms import upload
# from flower_detection.function.function import handle_uploaded_file


# Create your views here.
def home(request):
	if request.method =='POST':
		form = predictForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
	form =	predictForm()

	print("done")
	messages.success( request, (" You have successfully uploaded the image!"))
	return render(request, 'home/home.html',{'form':form})

def info_daisy(request):
	if request.method == 'GET':
		f_Info = Info.objects.get(Flower_name="DAISY")
	return render(request, 'home/info.html',{'info':f_Info})


def info_rose(request):
	if request.method == 'GET':
		f_Info = Info.objects.get(Flower_name="ROSE")
	return render(request, 'home/info.html',{'info':f_Info})

def info_dandelion(request):
	if request.method == 'GET':
		f_Info = Info.objects.get(Flower_name="DANDELION")
	return render(request, 'home/info.html',{'info':f_Info})

def info_sunflower(request):
	if request.method == 'GET':
		f_Info = Info.objects.get(Flower_name="SUNFLOWER")
	return render(request, 'home/info.html',{'info':f_Info})	

def info_tulip(request):
	if request.method == 'GET':
		f_Info = Info.objects.get(Flower_name="TULIP")
	return render(request, 'home/info.html',{'info':f_Info})

def info_lotus(request):
	if request.method == 'GET':
		f_Info = Info.objects.get(Flower_name="LOTUS")
	return render(request, 'home/info.html',{'info':f_Info})		

def upload(request):
	if request.method =='POST':
		form = predictForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	form =	predictForm()
	print("done")
	return render(request, 'home/home.html',{'form':form})

 
def About(request):
	return render(request, 'home/About.html')

def Help(request):
	return render(request, 'home/Help.html')

def dectection(request):
	p_data = predict.objects.last()
	global path
	path = p_data.Img_pre
	print(path)
	global a
	a=str(path)
	print(a)
	print(type(a))
	
	def dectection1():
		num_classes = 5

		model = tf.keras.Sequential([
		tf.keras.layers.experimental.preprocessing.Rescaling(1./255),
		tf.keras.layers.Conv2D(32, 3, activation='relu'),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Conv2D(32, 3, activation='relu'),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Conv2D(32, 3, activation='relu'),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Flatten(),
		tf.keras.layers.Dense(128, activation='relu'),
		tf.keras.layers.Dense(num_classes)
		])
	
		model = load_model(r"flower_detection\flower_api_model.h5")
		validation_image = image.load_img(r"C:/Users/tkada/OneDrive/Documents/Tejas Clg/Projects/internship/Django_Gui/media/" + a , target_size=(180,180))
		validation_image = image.img_to_array(validation_image)
		validation_image = np.expand_dims(validation_image,axis=0)
		result = model.predict(validation_image)
		

		y_predicted = model.predict(validation_image)
		y_predicted[0]

	
		global cn
		global flowername
		cn=np.argmax(y_predicted[0])
		if cn==0 :
			flowername =  'DAISY'
		elif cn==1 :
			flowername ='DANDELION'
		elif cn==2 :
			flowername ='ROSE'
		elif cn==3 :
			flowername = 'SUNFLOWER'
		elif cn==4 :
			flowername ='TULIP'
	dectection1()
	context = {	
			"flower_name" : flowername
		}

	print(path)
	print(type(path))
	print(flowername)

	if request.method == 'GET':
		f_Info = Info.objects.get(Flower_name=flowername)
		
		print(f_Info.Img)
		print(type(f_Info.Img))
	
		return render(request, 'home/detected.html',{'info':f_Info})
	