import pytest
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generated_code import get_weather_data

def test_get_weather_data():
    response = get_weather_data('London')
    assert response is not None
    assert isinstance(response, float)
    
