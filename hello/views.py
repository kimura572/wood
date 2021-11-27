from re import M
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from datetime import timezone
from .models import Photo, Member
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
      'form': '',
      'name':''
      }
  def get(self, request):
    if request.method == "GET":
      customers = list(Member.objects.all().values_list("species_name",flat=True))
      customers = ','.join(customers)
      self.params['name']=customers
    return render(request, 'hello/index.html', self.params)

  def post(self, request):
    if request.method == "POST":
      name = request.POST['dame']
      datab = Member()
      if not name in list(Member.objects.all().values_list("species_name",flat=True)):
        datab.species_name = name
        datab.save()
      image = request.FILES.get('image')
      save_image = Image.open(image)
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