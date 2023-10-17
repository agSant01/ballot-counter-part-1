import unittest
import logging

from src.array_list.array import ArrayList


class ArrayListTest(unittest.TestCase):
    def test_append_size(self):
        aL = ArrayList()
        aL.append(1)
        self.assertEqual(aL.count, 1)
        self.assertEqual(aL.getElement(0), 1)

    def test_print(self):
        aL = ArrayList()
        aL.append(1)
        aL.append(2)
        self.assertEqual(str(aL), '<ArrayList items: [1, 2]>')

    def test_insert_first(self):
        aL = ArrayList()
        aL.append(1)
        aL.append(2)
        aL.insert(0, 5)
        self.assertEqual(str(aL), '<ArrayList items: [5, 1, 2]>')
        aL.insert(2, 6)
        self.assertEqual(str(aL), '<ArrayList items: [5, 1, 6, 2]>')

    def test_insert_on_max(self):
        aL = ArrayList(3)
        self.assertEqual(aL.count, 0)
        self.assertEqual(aL.size, 3)

        aL.append(1)
        self.assertEqual(aL.count, 1)
        self.assertEqual(aL.size, 3)

        for i in range(2, 5):
            aL.append(i)
            self.assertEqual(aL.count, i)

        self.assertEqual(aL.size, 12)
        self.assertEqual(len(aL.array), 12)

    def test_get_element(self):
        aL = ArrayList()
        for i in range(5):
            aL.append(i)

        for i in range(5):
            self.assertEqual(aL.getElement(i), i)

    def test_remove(self):
        aL = ArrayList()
        for i in range(1, 10):
            aL.append(i)

        self.assertEqual(
            str(aL), '<ArrayList items: [1, 2, 3, 4, 5, 6, 7, 8, 9]>')

        self.assertEqual(aL.remove(0), 1)
        self.assertEqual(aL.getElement(0), 2)

        self.assertIsNone(aL.remove(20))  # silent fail, just return None

        self.assertEqual(aL.remove(4), 6)
        self.assertEqual(aL.count, 7)


if __name__ == "__main__":
    unittest.main()
    print('FUCK')
