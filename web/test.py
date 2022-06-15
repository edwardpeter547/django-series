from email import message
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
import os

class TestConfig(TestCase):
    
    def test_secret_key_strength(self):
        
        # self.assertEqual(SECRET_KEY, "django-insecure-@6=xr$m!v#jdndid76no)mf-g-+@+00_-i!darg0-0#id6(8+5")
        
        try:
            SECRET_KEY = str(os.environ.get('DJANGO_SECRET_KEY'))
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Weak Secret Key {e.messages}" #type: ignore
            self.fail(msg)