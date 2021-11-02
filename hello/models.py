from django.db import models
from datetime import datetime
import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import cv2
import shutil
import random

# Create your models here.
class Photo:
    def upload(save_image, name):
      SAVE_DIR = name
      if not os.path.isdir('images/'+SAVE_DIR):
        os.mkdir('images/'+SAVE_DIR)
      filepath = datetime.now().strftime('%Y%m%d_%H%M%S') + '.jpg'
      save_path = os.path.join(SAVE_DIR, filepath)
      save_image.save('images/'+save_path)
    
    def cut_image(save_image):
      SAVE_DIR2 = 'cut_image'
      if not os.path.isdir(SAVE_DIR2):
        os.mkdir(SAVE_DIR2)
      width = save_image.size[0]
      height = save_image.size[1]
      if height <= width:
        cut1 = random.randint(0,width-height)
        save_image1 = save_image.crop((cut1, 0, cut1+height, height))
      else:
        cut1 = random.randint(0,height-width)
        save_image1 = save_image.crop((0, cut1, width, cut1+width)) 
      img_resize = save_image1.resize((640, 640))
      f = 0
      for k in range(10):
          for l in range(10):
              im_crop = img_resize.crop((64*l, 64*k, 64*(l+1), 64*(k+1)))
              im_crop.save(SAVE_DIR2+'/'+str(f)+'.jpg', quality=95, dpi=(72,72)) 
              f += 1

    def Test_data():
      SAVE_DIR2 = 'cut_image'
      im_size = 64
      test_len = 100
      test_data = np.empty((test_len*1,im_size,im_size,1))
      s = os.listdir(SAVE_DIR2)
      c = 0
      for k in range(len(s)):
          fname = SAVE_DIR2+'/'+s[k]
          im = cv2.imread(fname)/ 255
          im = 0.299 * im[:,:,2] + 0.587 * im[:,:,1] + 0.114 * im[:,:,0]      
          im = np.expand_dims(im, axis=2)
          test_data[c,:,:,:] = im[:,:]
          c += 1
      shutil.rmtree(SAVE_DIR2+'/')
      return test_data

    def predict(test_data):
      model = load_model('/Users/fumiyakimura/Desktop/wood/hello/differ.h5')
      predict = model.predict(test_data)
      sum = 0
      for k in range(100):
        sum += predict[k][:]
      s = np.argmax(sum)
      cls = {0:'japonica (Sieb. et Zucc.) Hara', 1:'oxyphyllus Miq', 2:'arguta (Sieb. et Zucc.) Planch. ex Miq', 
      3:'australis Poir', 4:'barvinervis Sieb. et Zucc', 5:'commixta Hedl', 6:'controversa (Hemsl.) Sojak',
      7:'crenata Sieb.et Zucc', 8:'crispula Blume', 9:'elata (Miq.) Seemann', 10:'erecta Thunb', 11:'erythrocarpa Makino',
      12:'furcatum Blume ex Maxim', 13:'grayana Maxim',14:'grossa Sieb. et Zucc', 15:'hydrangeoides Sieb. et Zucc',
      16:'jamasakura Sieb. ex Koidz', 17:'japonica (Thunb.) Kanitz', 18:'japonica L', 19:'japonica Sieb. et Zucc',
      20:'japonica Thunb', 21:'japonicum Sieb. et Zucc', 22:'japonicum Sieb. ex Nakai', 23:'japonicum Thunb', 
      24:'javanica L', 25:'laxiflora (Sieb. et Zucc.) Bl', 26:'macrophylla (Wall.) Sojak', 27:'macropoda Miq', 
      28:'mono Maxim', 29:'multiflora Thunb', 30:'onoei Makino', 31:'orbiculatus Thunb', 32:'ovalifolia (Wall.) Drude',
      33:'paniculata Sieb. et Zucc', 34:'piperitum (L.) DC', 35:'polyandra Sieb. et Zucc', 36:'polycarpa Maxim', 
      37:'praecox Sieb. et Zucc', 38:'salicina Blume', 39:'scabra Thunb', 40:'serrata (Thunb. ex Murray) Ser',
      41:'serrata Thunb. ex Murray', 42:'sieboldiana Blume', 43:'sieboldianum Miq', 44:'teijsmannii Zoll. ex Kurz',
      45:'trichocarpa Miq', 46:'trichotomum Thunb', 47:'tschonoskii Maxim', 48:'umbellata Thunb',
      49:'villosa (Thunb.) Decne'}

      result = cls[s]
      prediction = round(max(sum),1)
      return result, prediction