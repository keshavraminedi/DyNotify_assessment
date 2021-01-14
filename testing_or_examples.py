# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:38:36 2021

@author: dell
"""
import requests
import json


test_url1 = 'http://localhost:5000/api/test'
#requesting API KEY
x=requests.get(test_url1)
x=json.loads(x.text)['api_key']
# a FEW examples

# send http request with images(as url or local image)  and receive response

s=json.dumps({'image1':"https://m.media-amazon.com/images/M/MV5BODcwNWE3OTMtMDc3MS00NDFjLWE1OTAtNDU3NjgxODMxY2UyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",'image2':"https://m.media-amazon.com/images/M/MV5BODcwNWE3OTMtMDc3MS00NDFjLWE1OTAtNDU3NjgxODMxY2UyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",'api_key':str(x)})
response = requests.post(test_url1, json=s)
print(json.loads(response.text))

s=json.dumps({'image1':"https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",'image2':"https://media2.s-nbcnews.com/j/streams/2013/March/130326/1C6639340-google-logo.nbcnews-fp-1024-512.jpg",'api_key':str(x)})
response = requests.post(test_url1, json=s)
print(json.loads(response.text))

s=json.dumps({'image1':"https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",'image2':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8Gd1KivcOPCai64qWDFnpOM0eUaKBs776vQ&usqp=CAU",'api_key':str(x)})
response = requests.post(test_url1, json=s)
print(json.loads(response.text))

