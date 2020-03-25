import unittest
import converter


class converterTest(unittest.TestCase):

    def test_invalid_type_input(self):
        self.assertRaises(ValueError, converter.convert_arabic_to_roman, "Roman")

    def test_input_zero(self):
        self.assertRaises(ValueError, converter.convert_arabic_to_roman, 0)

    def test_negative_input_without_param(self):
        self.assertRaises(ValueError, converter.convert_arabic_to_roman, -40)

    def test_input_greater_than_max_limit(self):
        self.assertRaises(ValueError, converter.convert_arabic_to_roman,
                          converter.MAX_NUM_TO_CONVERT+1)

    def test_input_positive_integer(self):
        self.assertEqual("CXXVII", converter.convert_arabic_to_roman(127))

    def test_input_float(self):
        self.assertEqual("XXXVII", converter.convert_arabic_to_roman(37.75))

    def test_input_max_limit_positive(self):
        self.assertEqual("MMMCMXCIX", converter.convert_arabic_to_roman(3999))

    def test_input_negative(self):
        self.assertEqual("-CXXVII", converter.convert_arabic_to_roman(-127, True))

    def test_input_float_negative(self):
        self.assertEqual("-XXXVII", converter.convert_arabic_to_roman(-37.75, True))

    def test_input_max_limit_negative(self):
        self.assertEqual("-MMMCMXCIX", converter.convert_arabic_to_roman(-3999, True))


if __name__ == "__main__":
    unittest.main()