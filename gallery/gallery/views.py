from django.shortcuts import render
from .models import Image,Category,Location
import numpy as np
from django.core.exceptions import ObjectDoesNotExist

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

def search_results(request):
  if 'category' in request.GET and request.GET["category"]:
    search=request.GET.get("category")
    try:
      category=Category.objects.get(name=search)
      images=Image.search_image(category)
      arr= np.array(images) 
      newarr = np.array_split(arr,3)
      first = newarr[0]
      second = newarr[1]
      third = newarr[2]
      message = f"Found {len(images)} image(s) under the category - {search}"
      return render(request, 'search.html',{"message":message,"images": images,"first": first,"second": second,"third": third})
    except ObjectDoesNotExist:
      message = "NO ITEMS UNDER CATEGORY " + search.upper()
      categories = Category.objects.all()
      return render(request, 'search.html',{"message":message, "categories": categories})
  
  else:
    message = "You haven't searched for any category"
    return render(request, 'search.html',{"message":message})