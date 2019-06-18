from flask import json, Response
from flask_hal import HAL, document
from pprint import pprint

def getSelfLink(routeObject):
  HAL(routeObject)
  resp_document = document.Document()
  return resp_document.to_dict()['_links']

def formatResponse(routeObject, data):
  response = Response(json.dumps({'_embedded': data, '_links': getSelfLink(routeObject)}, ensure_ascii=False), 
           status=200,
           mimetype='application/json')
  return response
