import sys
    sys.path.append ('/Users/leeco/Downloads/adt-bundle-mac-x86_64-20140702/sdk/tools/')
from uiautomator import device as d
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        print("begin")
    def tearDown(self):
        print("test ending")
    def test_first(self):
        d.screen.on()
        d(text="QQ").click()
        print("test finish")
    def test_second(self):
        login()
        print ("login test")           
    def test_third(self):
        doSthing()
        print ("test 4 finish"  )       

if __name__ == '__main__':
        unittest.main()