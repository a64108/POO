from unittest import TestCase
from helloworld import get_greetings


class TestHelloWorld(TestCase):
    def test_get_greetings(self):
        self.assertEqual(get_greetings(), "Hello World!")


# Opcional
if __name__ == "__main__":
    import unittest

    unittest.main(verbosity=2)
