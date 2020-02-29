from flask import Flask,request,render_template
import os
from encode_faces import *
from api import api
from recognize_faces_image import *

app=Flask(__name__)


app.register_blueprint(api,url_prefix="/api")

@app.route('/',methods=['get','post'])
def faceupload():
	if 'submit' in request.form:
		val=request.form['val']
		image=request.files['image']
		# path = 'static/uploads/'
		path=""
		# Check whether the   
		# specified path is   
		# an existing file 
		isFile = os.path.isdir("static/uploads/"+val)  
		print(isFile)
		if(isFile==False):
			os.mkdir('static\\uploads\\'+val)
		path="static/uploads/"+val+"/"+image.filename
		image.save(path)


	if 'train' in request.form:
		enf("static/uploads/")


	if 'check' in request.form:
		print("hg")
		vals=request.form['vals']
		image=request.files['image']

		path="static/uploads/"+image.filename
		image.save(path)

		val=rec_face_image(path)
		print(val)
		if vals in val:
			print("success")
	return render_template('fileupload.html')



app.run(debug=True,port=5002)










