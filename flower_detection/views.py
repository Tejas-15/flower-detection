from django.shortcuts import render
from django.http import HttpResponse
from .models import Info

#tenserflow
from tensorflow.python.eager.context import context
import win32gui
from PIL import ImageGrab, Image
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf

#models
from flower_detection.models import Info

# #upload 
# from flower_detection.forms import upload
# from flower_detection.function.function import handle_uploaded_file


# Create your views here.
def home(request):
	return render(request, 'home/home.html')

# def upload(request):
# 	print("hi")
# 	if request.method =='POST':
# 		uploaded_file = request.FILES['document']
# 		print(uploaded_file.name)
# 	return render(request, 'home/upload.html')
 
def About(request):
	return render(request, 'home/About.html')

def daisy(request):
	return render(request, 'home/daisy.html')

def yellow_rose(request):
	return render(request, 'home/yellow_rose.html')

def rose(request):
	all_Info = Info.objects.all
	return render(request, 'home/rose.html',{'all':all_Info})

def hometest(request):
	return render(request, 'home/test3.html')	

def	flower_info(request):
	f_info = Info.objects.get(pk=1)
	print('Myoutput',f_info)
	return render(request, 'home/test1.html',{'info':f_info})


def Test1(request):
	def predict():
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
		validation_image = image.load_img(r"C:\Users\tkada\OneDrive\Documents\Tejas Clg\Projects\object detection\New folder\dandaliom\gettyimages-947528850-612x612.jpg", target_size=(180,180))
		validation_image = image.img_to_array(validation_image)
		validation_image = np.expand_dims(validation_image,axis=0)
		result = model.predict(validation_image)
		

		y_predicted = model.predict(validation_image)
		y_predicted[0]

	
		global cn
		global flowername
		cn=np.argmax(y_predicted[0])
		if cn==0 :
			flowername =  'daisy'
		elif cn==1 :
			flowername ='dandelion'
		elif cn==2 :
			flowername ='Rose'
		elif cn==3 :
			flowername = 'sunflower'
		elif cn==4 :
			flowername ='tulip'
	predict()
	context = {	
			"flower_name" : flowername
		}
	if 	flowername ==  'daisy' :
		return render(request, 'home/daisy.html',context)
	elif 	flowername == 'dandelion' :
		return render(request, 'home/yellow_rose.html',context)
		
# def formsubmission(request):
# 	print("hi")
# 	form=upload()
# 	if request.method=="POST":
# 		form=upload(request.POST,request.FILES)
# 		if form.is_valid():
# 			handle_uploaded_file(request.FILES['file'])
# 			return HttpResponse("File uploaded successfully")

# 		else:
# 			form=upload()

	# return render(request,'home/test1.html',{'form':form})
