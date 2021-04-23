from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FormSerializer
from .models import Form
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
import os

# Create your views here.

class FormView(viewsets.ModelViewSet):
  serializer_class = FormSerializer
  queryset = Form.objects.all()

class FrontEndAppView(View):
  def get(self, request):
    print (os.path.join(settings.REACT_APP_DIR, 'build', 'index.html'))
    try:
      with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html') as f:
        return HttpResponse(f.read())
    except FileNotFoundError:
      logging.exception('build of app not found')
      return HttpResponse(status=501)

# class Assets(View):

#   def get(self, _request, filename):
#     path = os.path.join(os.path.dirname(__file__), 'static', filename)

#     if os.path.isfile(path):
#       with open(path, 'rb') as file:
#         return HttpResponse(file.read(), content_type='application/javascript')
    
#     else:
#       return HttpResponseNotFound()