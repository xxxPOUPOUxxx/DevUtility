# test_devutility.py
"""
Tests for DevUtility module.
"""

import unittest
from devutility import DevUtility

class TestDevUtility(unittest.TestCase):
    """Test cases for DevUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DevUtility()
        self.assertIsInstance(instance, DevUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DevUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
