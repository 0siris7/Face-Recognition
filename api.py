from flask import Blueprint
import os
from recognize_faces_image import *

api=Blueprint('api',__name__)
@api.route('/facecheck/',methods=['get','post'])
def facecheck():
	print("hg")
	vals=request.form['vals']
	image=request.files['image']

	path="static/uploads/"+image.filename
	image.save(path)

	val=rec_face_image(path)
	print(val)
	if vals in val:
		out=1
	else:
		out=0
	data['res']=out
	data['status']="success"
	return demjson.encode(data)


