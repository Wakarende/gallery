from django.test import TestCase
from .models import Location,Category,Image


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
  
  def test_update_category(self):
    """
    Test that determines whether the category has been updated
    """
    self.fashion.save_category()
    self.fashion.update_category(self.fashion.id, 'travel')
    update = Category.objects.get(name='travel')
    self.assertEqual(update.name, 'travel')





class ImageTest(TestCase):
  def setUp(self):
    self.category= Category(name='interior')
    self.category.save_category()
    self.location= Location(name='nairobi')
    self.location.save_location()
    self.image= Image(id='1', name='kitchen',description='description',photo='image.png',category=self.category,location=self.location)

  def tearDown(self):
    """
    Clears Database after each test
    """
    Image.objects.all().delete()
    Category.objects.all().delete()
    Location.objects.all().delete()
  
  def test_image_instance(self):
    """
    test that determines whether a new image created is an instance of the Image class
    """
    self.assertTrue(isinstance(self.image, Image))

  def test_save_image(self):
    """
    Test whether new image is added to the db
    """
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)
  
  def tearDown(self):
    """
    Clears Database after each test
    """
    Image.objects.all().delete()
    Category.objects.all().delete()
    Location.objects.all().delete()


  def test_delete_image(self):
    """
    Test whether image is deleted
    """

    self.image.save_image()
    images=Image.objects.all()
    self.assertEqual(len(images),1)
    self.image.delete_image()
    del_images=Image.objects.all()
    self.assertEqual(len(del_images),0)


  def test_search_category(self):
    '''
    Tests whether image is retrieved by category
    '''
    self.location = Location(name='nairobi')
    self.location.save_location()
    self.category = Category(name='interior')
    self.category.save_category()
    self.image=Image(id=1,photo="image.png",name='kitchen',description='description',location=self.location,category=self.category)
    self.image.save_image()
    images=Image.search_image(self.category.id)
    self.assertTrue(len(images)> 0)
  
  def test_search_location(self):
    # self.location = Location(name='nairobi')
    self.location.save_location()
    self.category = Category(name='interior')
    self.category.save_category()
    self.image=Image(id=1,photo="image.png",name='kitchen',description='description',location=self.location,category=self.category)
    self.image.save_image()
    images = Image.filter_by_location("nairobi")
    self.assertTrue(len(images) > 0)