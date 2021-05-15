from django.shortcuts import render
from .models import Image,Category,Location
import numpy as np

# Create your views here.
def home(request):
  images = Image.objects.all()
  arr= np.array(images) 
  newarr = np.array_split(arr,3)
  first = newarr[0]
  second = newarr[1]
  third = newarr[2]
  locations = Location.objects.all()
  categories = Category.objects.all()
  return render(request,'home.html',{"first": first,"second": second,"third": third,"locations":locations,"categories": categories})