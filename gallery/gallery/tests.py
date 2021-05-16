from django.test import TestCase
from .models import Location,Category,Image
from django.test import override_settings

# Create your tests here.
class LocationTest(TestCase):
  def setUp(self):
    '''
    create new instances before a test
    '''
    self.nairobi = Location(name = "Nairobi")
    self.nakuru = Location(name = "Nakuru")

  def tearDown(self):
    '''
    clear database after each test
    '''
    Location.objects.all().delete()

  def test_location_instance(self):
    '''
    test whether the new location created is an instance of the Location class
    '''
    self.assertTrue(isinstance(self.nairobi, Location))
    
  def test_save_location(self):
    '''
    test whether new locations are added to the db 
    '''
    self.nairobi.save_location()
    self.nakuru.save_location()
    locations = Location.objects.all()
    self.assertEqual(len(locations),2)

  def test_delete_location(self):
    '''
    test whether a location is deleted
    '''
    self.nairobi.save_location()
    locations1= Location.objects.all()
    self.assertEqual(len(locations1),1)
    self.nairobi.delete_location()
    locations2= Location.objects.all()
    self.assertEqual(len(locations2),0)

  def test_update_location(self):
    '''
    test whether the location name is updated
    '''
    self.nairobi.save_location()
    self.nairobi.update_location(self.nairobi.id,'Arusha')
    update = Location.objects.get(name = "Arusha")
    self.assertEqual(update.name, 'Arusha')

  def test_display_locations(self):
    '''
    This tests whether the display location function is getting the locations from the db
    '''
    self.nairobi.save_location()
    self.nakuru.save_location()
    self.assertEqual(len(Location.display_all_locations()), 2)

class CategoryTest(TestCase):
  def setUp(self):
    """
    Creates new instance before a test
    """
    self.fashion = Category(name='fashion')
    self.games = Category(name='games')

  def tearDown(self):
    """
    Clears database after each test
    """
    Category.objects.all().delete()

  def test_category_instance(self):
    """
    Test whether the new categories an an instance of the category class
    """
    self.assertTrue(isinstance(self.fashion, Category))
    self.assertTrue(isinstance(self.games, Category))

  def test_save_category(self):
    """
    Test that determines whehter new categories are saved to the db
    """
    self.fashion.save_category()
    self.games.save_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories) == 2)

  def test_delete_category(self):
    """
    Test whether category is deleted
    """
    self.fashion.save_category()
    self.games.save_category()
    categories1 = Category.objects.all()
    self.assertEqual(len(categories1),2)
    self.fashion.delete_category()
    categories2 = Category.objects.all()
    self.assertEqual(len(categories2),1)




# class ImageTest(TestCase):
#   def setup(self):
#     self.new_category= Category(name='interior')
#     self.new_location= Location(name='nairobi')
#     self.new_image= Image(name='kitchen',description='description',photo='image.png',category='interior',location='nairobi')

#   def tearDown(self):
#     """
#     Clears Database after each test
#     """
#     Image.objects.all().delete()
#     Category.objects.all().delete()
#     Location.objects.all().delete()
  
#   def test_image_instance(self):
#     """
#     test that determines whether a new image created is an instance of the Image class
#     """
#     self.assertTrue(isinstance(self.new_image, Image))

#   def test_save_image(self):
#     """
#     Test whether new image is added to the db
#     """
#     self.new_image.save_image()
#     all_objects = Image.objects.all()
#     self.assertTrue(len(all_objects)>0)
  




