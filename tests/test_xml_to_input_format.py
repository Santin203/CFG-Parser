import unittest
from src.xml_to_input_format import *

class TestXmlToInputFormat(unittest.TestCase):
    def test_conversion_to_input_format_xml(self):
        input_file_name = "xml_test1.xml"
        output_file_name = "input.txt"
        
        conversion_to_input_format(input_file_name)
        
        with open(output_file_name, 'r') as f:
            text = f.read()
        self.assertEqual(text, '<a><b><c>text1</c><c>text2</c>a</b></a>')
        
        
    def test_conversion_to_input_format_html(self):
        input_file_name = "html_test1.html"
        output_file_name = "input.txt"
        
        conversion_to_input_format(input_file_name)
        
        with open(output_file_name, 'r') as f:
            text = f.read()
        self.assertEqual(text, '<html lang="n" id="n">n</html>')
        
if __name__ == '__main__':
    unittest.main()