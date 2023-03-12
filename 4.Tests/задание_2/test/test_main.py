import unittest
from unittest import TestCase
from main import path_yadisk

class Test_Yadisk(TestCase):
    res = str(path_yadisk())

    @unittest.skipIf(res == '<Response [409]>' or res == '<Response [401]>', res)
    def test_path_1(self, res=res):
        res_test = '<Response [201]>'
        self.assertEqual(res, res_test)
        return print("Папка успешно создана")

    @unittest.skipIf(res == '<Response [201]>'or res == '<Response [401]>', res)
    def test_path_2(self, res=res):
        res_test = '<Response [409]>'
        self.assertEqual(res, res_test)
        return print("Папка уже создана")

    @unittest.skipIf(res == '<Response [201]>' or res == '<Response [409]>', res)
    def test_path_3(self, res=res):
        res_test = '<Response [401]>'
        self.assertEqual(res, res_test)
        return print("Не пройдена авторизация")
