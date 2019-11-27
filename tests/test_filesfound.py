
from unittest import TestCase
from filesfound.typeoffiles.typeoffiles import count_types, find_in_path


class TestConsole(TestCase):
    def setUp(self):
        self.path = "/home/user/PycharmProjects/filesfound/tests/test"

    def test_find_size(self):
        types = ["image/jpeg",]
        size = True
        all_values, all_size = count_types(types, self.path, size)
        self.assertEqual(all_size,5705)
        self.assertEqual(all_values, {'/home/user/PycharmProjects/filesfound/tests/test/index.jpeg':5705})

    def test_find_size_non_types(self):
        types = []
        size = True
        all_values, all_size = count_types(types, self.path, size)
        self.assertEqual(all_size, 5778)
        self.assertEqual(all_values, {'/home/user/PycharmProjects/filesfound/tests/test/3.txt':16,
                                      '/home/user/PycharmProjects/filesfound/tests/test/text.txt':11,
                                      '/home/user/PycharmProjects/filesfound/tests/test/2.txt':46,
                                      '/home/user/PycharmProjects/filesfound/tests/test/index.jpeg':5705
                                      })

    def test_count_types(self):
        types = ["image/jpeg",]
        size = False
        all_types, all_count = count_types(types, self.path, size)
        self.assertEqual(all_types, {'image/jpeg':1})
        self.assertEqual(all_count, 1)

    def test_count_types_non_types(self):
        types = []
        size = False
        all_types, all_count = count_types(types, self.path, size)
        self.assertEqual(all_types, {'text/plain':3,
                                     'image/jpeg':1,
                                    })
        self.assertEqual(all_count, 4)

    def test_find_in_path(self):
        path = "/home/user/PycharmProjects/filesfound/tests/empty"
        all = find_in_path(path)
        self.assertRaises(ValueError)
