import unittest

x = int(input("Введите x "))
y = int(input("Введите y "))
x1 = int(input("Введите x1 "))
y1 = int(input("Введите y1 "))


def rastoyanie(x, y, x1, y1):
    z = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    return z


class TestDistance(unittest.TestCase):

    def testZeroValue(self):
        res = rastoyanie(0, 0, 0, 0)
        self.assertEqual(res, 0)

    def Test(self):
        res = rastoyanie(0, 0, 0, 1)
        self.assertEqual(res, 10)


if __name__ == '__main__':
    unittest.main()





