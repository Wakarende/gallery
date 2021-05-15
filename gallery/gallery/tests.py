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

