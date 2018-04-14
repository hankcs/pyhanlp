import unittest

from pyhanlp import HanLP, CustomDictionary


class CustomDictionaryTestCase(unittest.TestCase):
    def test_custom_dict_forcing(self):
        segment = HanLP.newSegment('viterbi')
        CustomDictionary.insert('川普', 'nr 1')
        self.assertIn('四川/ns, 普通人/n, 与/cc, 川/b, 普通/a, 电话/n', segment.seg('四川普通人与川普通电话').__str__())
        segment.enableCustomDictionaryForcing(True)
        self.assertIn('四川/ns, 普通人/n, 与/cc, 川普/nr, 通电话/vi', segment.seg('四川普通人与川普通电话').__str__())


if __name__ == '__main__':
    unittest.main()
