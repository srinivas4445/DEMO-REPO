def logincheck(uname, pwd):

    if(uname=='admin' and pwd=='admin123'):
        return 'success'

    if(uname!='admin' and pwd=='admin123'):
        return 'uname fail'
    if(uname=='admin' and pwd!='admin123'):
        return 'pwd fail'
    if(uname!='admin' and pwd!='admin123'):
        return 'uname pwd fail'

import unittest

class loginclass(unittest.TestCase):
    def test1(self):

        result = logincheck('admin', 'admin123')

        self.assertEqual(result, 'success')

    def test2(self):

        result = logincheck('admin', '1234')

        self.assertEqual(result, 'pwd fail')

    def test3(self):

        result = logincheck('abc', 'admin123')

        self.assertEqual(result, 'uname fail')

    def test4(self):

        result = logincheck('abc', '1234')

        self.assertEqual(result, 'uname pwd fail')

if __name__  == '__main__':

    unittest.main()
