import os
import unittest
from cigam import Magic

FILES_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'files' + os.sep


class TestMagic(unittest.TestCase):

    def test_apk(self):
        m = Magic(FILES_PATH + 'test.apk')
        self.assertEqual(m.get_type(), 'apk')

    def test_axml(self):
        m = Magic(FILES_PATH + 'test.axml')
        self.assertEqual(m.get_type(), 'axml')

    def test_arsc(self):
        m = Magic(FILES_PATH + 'test.arsc')
        self.assertEqual(m.get_type(), 'arsc')

    def test_elf(self):
        m = Magic(FILES_PATH + 'test.so')
        self.assertEqual(m.get_type(), 'elf')

    def test_dex(self):
        m = Magic(FILES_PATH + 'test.dex')
        self.assertEqual(m.get_type(), 'dex')

    def test_zip(self):
        m = Magic(FILES_PATH + 'test.zip')
        self.assertEqual(m.get_type(), 'zip')

    def test_tar(self):
        pass

    def test_png(self):
        m = Magic(FILES_PATH + 'test.png')
        self.assertEqual(m.get_type(), 'png')

    def test_gif(self):
        pass

    def test_ogg(self):
        pass

    def istext(self, data):
        m = Magic(FILES_PATH + 'test.txt')
        self.assertEqual(m.get_type(), 'txt')

if __name__ == '__main__':
    unittest.main()
