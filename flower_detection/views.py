
from django.shortcuts import render
from django.http import HttpResponse

#models
from .models import Info
from .models import predict


#tenserflow
from tensorflow.python.eager.context import context
import win32gui
from PIL import ImageGrab, Image
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf



# #upload 
# from flower_detection.forms import upload
# from flower_detection.function.function import handle_uploaded_file


# Create your views here.
def home(request):
	p_data = predict.objects.get(pk=1)
	global path
	path = p_data.Img_pre
	print(path)
	return render(request, 'home/home.html',{'data':p_data})

# def upload(request):
# 	print("hi")
# 	if request.method =='POST':
# 		uploaded_file = request.FILES['document']
# 		print(uploaded_file.name)
# 	return render(request, 'home/upload.html')
 
def About(request):
	return render(request, 'home/About.html')

# def	data(request):
	
# 	# print(p_Info.Img_pre)
# 	# print(flowername)
# 	return render(request, 'home/about.html')

def dectection(request):
	
	
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
		validation_image = image.load_img(r"C:\Users\tkada\OneDrive\Documents\Tejas Clg\Projects\Django_Gui\Django_Gui\media\images\rose1.jpg" , target_size=(180,180))
		validation_image = image.img_to_array(validation_image)
		validation_image = np.expand_dims(validation_image,axis=0)
		result = model.predict(validation_image)
		

		y_predicted = model.predict(validation_image)
		y_predicted[0]

	
		global cn
		global flowername
		cn=np.argmax(y_predicted[0])
		if cn==0 :
			flowername =  'Daisy'
		elif cn==1 :
			flowername ='dandelion'
		elif cn==2 :
			flowername ='rose'
		elif cn==3 :
			flowername = 'sunflower'
		elif cn==4 :
			flowername ='tulip'
	predict()
	context = {	
			"flower_name" : flowername
		}

	print(path)
	print(flowername)


	f_Info = Info.objects.get(Flower_name=flowername)
	
	print(f_Info.Img)
	
	return render(request, 'home/detected.html',{'info':f_Info})
	
		


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
