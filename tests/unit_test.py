import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generated_code import get_weather_data

class TestWeatherData(unittest.TestCase):

    def test_get_weather_data(self):
        # Mocking the requests.get response using unittest.mock
        from unittest.mock import patch
        
        mock_response = {
            'current': {
                'temp_c': 22.5
            }
        }

        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = mock_response
            result = get_weather_data('London')
            self.assertEqual(result, 22.5)  # Expecting temperature to be 22.5
            
if __name__ == '__main__':
    unittest.main()
