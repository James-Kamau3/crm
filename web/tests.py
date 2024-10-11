from django.test import TestCase
from django.contrib.auth.models import User
from .models import Record
from django.utils import timezone


class TestModel(TestCase):
    """
    setup before each test
    """
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test123@gmail.com', password='password')
        self.email = self.user.email  # Get the email as a string

    def test_model_Record(self):
        # Create a record instance
        record_item = Record.objects.create(
            first_name='test_firstname',
            last_name='test_lastname',
            email=self.email,  # Passing email as a string
            phone='1234567890',
            address='123 Test St',
            city='Test City',
            state='Test State',
            zipcode='12345'
        )

        # Test if the record is an instance of Record model
        self.assertTrue(isinstance(record_item, Record))

        # Test the string representation of the record
        self.assertEquals(str(record_item), 'test_firstname test_lastname')
        
        # Test if the fields are correctly assigned
        self.assertEqual(record_item.first_name, 'test_firstname')
        self.assertEqual(record_item.last_name, 'test_lastname')
        self.assertEqual(record_item.email, 'test123@gmail.com')
        self.assertEqual(record_item.phone, '1234567890')
        self.assertEqual(record_item.address, '123 Test St')
        self.assertEqual(record_item.city, 'Test City')
        self.assertEqual(record_item.state, 'Test State')
        self.assertEqual(record_item.zipcode, '12345')
        
        # Test if a record is created in the database
        self.assertEqual(Record.objects.count(), 1)
        
        # Test if created_at field is automatically populated
        self.assertTrue(record_item.created_at <= timezone.now())
        
        # Test for record deletion in db
        record_item.delete()
        self.assertEqual(Record.objects.count(), 0)


