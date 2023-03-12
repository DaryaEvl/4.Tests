import unittest
from unittest import TestCase
from main import task_1, task_2, task_4

class Task_1(TestCase):
    def test1_task_1(self):
        res = task_1()
        self.assertEqual(res, [['visit1'], ['visit3'], ['visit7'], ['visit8'], ['visit9'], ['visit10']])

    def test2_task_1(self):
        res = task_1()
        self.assertIsInstance(res, list)

    def test3_task_1(self):
        res = task_1()
        self.assertIsNot('visit2', res)

class Task_2(TestCase):
    def test1_task_2(self):
        res = task_2()
        self.assertEqual(res, [213, 15, 54, 119, 98, 35])

    def test2_task_2(self):
        res = task_2()
        self.assertIsInstance(res, list)

    def test3_task_2(self):
        res = task_2()
        res_test = set(res)
        self.assertEqual((len(res)), (len(res_test)))

class Task_4(TestCase):
    def test1_task_4(self):
        res = task_4()
        self.assertEqual(res, 'yandex')

    def test2_task_4(self):
        res = task_4()
        self.assertIsInstance(res, str)

    def test3_task_4(self):
        res = task_4()
        self.assertNotEqual(res, 'google')



