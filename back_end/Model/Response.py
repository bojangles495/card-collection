from flask import json
from flask_hal import HAL, document

def getSelfLink(routeObject):
  HAL(routeObject)
  resp_document = document.Document()
  return resp_document.to_dict()['_links']

def formatResponse(routeObject, data):
  return json.dumps({'_embedded': data, '_links': getSelfLink(routeObject)}, ensure_ascii=False)
