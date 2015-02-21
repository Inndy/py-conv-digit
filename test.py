import unittest

import convert

class FunctionTest(unittest.TestCase):

    def test_9527(self):
        self.assertEqual(9527, convert.uppercase_to_digits('玖仟伍佰貳拾柒'))

    def test_95278689(self):
        self.assertEqual(95278689, convert.uppercase_to_digits('玖仟伍佰貳拾柒萬捌仟陸佰捌拾玖'))

    def test_689000020009(self):
        self.assertEqual(68900002000, convert.uppercase_to_digits('陸佰捌拾玖億零貳仟'))

    def test_730000000(self):
        self.assertEqual(730000000, convert.uppercase_to_digits('柒億參仟萬元'))

    def test_170300(self):
        self.assertEqual(170300, convert.uppercase_to_digits('壹拾柒萬零參佰元'))

    def test_invalid_number(self):
        self.assertEqual(0, convert.uppercase_to_digits('嗡嗡嗡元'))



if __name__ == '__main__':
    unittest.main()
