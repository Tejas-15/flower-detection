from tensorflow.python.eager.context import context
import win32gui
from PIL import ImageGrab, Image
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	# return HttpResponse('<h2>world</h2>')
	return render(request, 'home/home.html')

def upload(request):
	if request.method =='POST':
		uploaded_file = request.FILES['document']
		print(uploaded_file.name)
		print("hi")
	return render(request, 'home/upload.html')
 
def test(request):
	return render(request, 'home/test.html')

def daisy(request):
	return render(request, 'home/daisy.html')

def yellow_rose(request):
	return render(request, 'home/yellow_rose.html')

def pink_rose(request):
	return render(request, 'home/pink_rose.html')

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
	
		model = load_model(r"C:\Users\tkada\OneDrive\Documents\MIni Project\Django_Gui\flower_detection\flower_api_model.h5")
		validation_image = image.load_img(r"C:\Users\tkada\OneDrive\Documents\MIni Project\Django_Gui\flower_detection\static\rose3.jpg", target_size=(180,180))
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
	return render(request, 'home/test1.html',context)
		