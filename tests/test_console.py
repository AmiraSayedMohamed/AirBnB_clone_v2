import unittest
from io import StringIO
import sys
import os
from console import HBNBCommand
from models import storage

class TestConsoleCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create_state(self):
        command = 'create State name="California"'
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Assuming UUID length
            # Check if State object was created and stored correctly
            state_id = output
            state = storage.all()["State." + state_id]
            self.assertEqual(state.name, "California")

    def test_create_place(self):
        command = 'create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297'
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Assuming UUID length
            # Check if Place object was created and stored correctly
            place_id = output
            place = storage.all()["Place." + place_id]
            self.assertEqual(place.name, "My little house")
            self.assertEqual(place.city_id, "0001")
            self.assertEqual(place.user_id, "0001")
            self.assertEqual(place.number_rooms, 4)
            self.assertEqual(place.number_bathrooms, 2)
            self.assertEqual(place.max_guest, 10)
            self.assertEqual(place.price_by_night, 300)
            self.assertEqual(place.latitude, 37.773972)
            self.assertEqual(place.longitude, -122.431297)

    def test_invalid_command(self):
        command = 'create InvalidClass'
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_invalid_parameters(self):
        command = 'create State invalid_param="value"'
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()


