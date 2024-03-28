from unittest import TestCase


class TestStringMethods(TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])

        # s.split should fail when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


# Opcional
if __name__ == "__main__":
    import unittest

    unittest.main(verbosity=2)
