# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:38:35 2021

@author: KESHAV RAMINEDI
"""
from flask import Flask, request, Response
import jsonpickle,json,requests
import numpy as np
import cv2
import numpy
import os
import validators
# Initialize the Flask application
app = Flask(__name__)
img=None
api_key=os.urandom(16)
# route http posts to this method
@app.route('/api/test', methods=['POST','GET'])
def test():
    
  r = request
  if r.method=='GET':
      response_pickled = jsonpickle.encode({'api_key':str(api_key)})
      #returning API KEY      
      return Response(response=response_pickled, status=200, mimetype="application/json")
  if r.method=='POST': 
    filestr1 = json.loads(r.get_json())
    #validating API KEY
    if filestr1['api_key']!=str(api_key):
        print(str(api_key))
        print(filestr1['api_key'])
        response_pickled = jsonpickle.encode({'error':"invalid api_key"})
        return Response(response=response_pickled, status=200, mimetype="application/json")
    npimg1=None
    npimg2=None
    if validators.url(str(filestr1['image1']))==True:
        img1=requests.get(filestr1['image1']).content
        img1 = numpy.frombuffer(img1, numpy.uint8)

        npimg1 = cv2.imdecode(img1, cv2.IMREAD_COLOR)
        print("first image is url")
    else:
        npimg1=cv2.imread(filestr1['image1'])
    if validators.url(filestr1['image2'])==True:
        img2=requests.get(filestr1['image2']).content
        img2 = numpy.frombuffer(img2, numpy.uint8)
        npimg2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)

        print("second image is url")
    else:
        npimg2=cv2.imread(filestr1['image2'])
    img1=npimg1
    img2=npimg2
    if img1.shape!=img2.shape:
        img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))
    #calculating the similarity of images............................    
    res = cv2.absdiff(img1,img2)
    res = res.astype(np.uint8)
    percentage =100-( (numpy.count_nonzero(res) * 100)/ res.size)
    print(percentage)
    # returning the JSON data
    response_pickled = jsonpickle.encode({'percentage':percentage})

    return Response(response=response_pickled, status=200, mimetype="application/json")
app.run(host="0.0.0.0", port=5000)