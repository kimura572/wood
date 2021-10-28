from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from datetime import timezone
from .models import Photo
from django.shortcuts import redirect
from django.views.generic import TemplateView
from PIL import Image


# Create your views here.
class HelloView(TemplateView):
  def __init__(self):
    self.params = {
      'title': 'wood classifier',
      'message' :'',
      'result':'',
      'value':'',
      'form': HelloForm()
    }
  def get(self, request):
    return render(request, 'hello/index.html', self.params)

  def post(self, request):
    if request.method == "POST":
      image = request.FILES.get('image')
      save_image = Image.open(image)
      name = request.POST['name']
      Photo.upload(save_image, name)
      Photo.cut_image(save_image)
      test_data = Photo.Test_data()
      s, l = Photo.predict(test_data)
      chk = '正解は<b>'+name+'</b>です。'
      self.params['form'] = HelloForm(request.POST)
      self.params['message'] = chk
      self.params['result'] = '予測結果は'+s+'です。'
      self.params['value'] = '予測精度は'+str(l)+'%です。'
    return render(request, 'hello/index.html', self.params)