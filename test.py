'''

test.py: Python testing to ensure correct formatting and varibles included for
         metadata in experiments.

The MIT License (MIT)

Copyright (c) 2016-2017 Vanessa Sochat, Stanford University

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import os
import re
import sys
from glob import glob
import json

from unittest import TestCase

VERSION = sys.version_info[0]
here = os.getcwd()

print("*** PYTHON VERSION %s BASE TESTING START ***" %(VERSION))

class TestLibrary(TestCase):

    def setUp(self):

        # Test repo information
        self.experiments_base = "%s/experiments" %(here) 
        self.experiments = glob("%s/*" %self.experiments_base)
        
        print("\nSTART-----------------------------------------")

    def tearDown(self):
        print("END---------------------------------------------")

    def test_validate_extension(self):
        '''test_validate_extension ensures that all files are json
        '''
        print("TEST: All files must be json")
        for jsonfile in self.experiments:
            print("Experiment %s" %(os.path.basename(jsonfile)))
            self.assertTrue(jsonfile.endswith('.json')) 


    def test_load_json(self):
        '''test_load_json ensures that all files load
        '''
        print("TEST: Files are valid json format")
        for jsonfile in self.experiments:
            print("Experiment %s" %(os.path.basename(jsonfile)))
            with open(jsonfile,'r') as filey:
                content = json.load(filey)
            self.assertTrue(isinstance(content,dict)) 

    def test_validate_json(self):
        '''test_validate_json ensures that all files have
        correct variables, naming, and fields
        '''
        print("TEST: Validate json content")
        for jsonfile in self.experiments:
            print("Experiment %s" %(os.path.basename(jsonfile)))
            with open(jsonfile,'r') as filey:
                content = json.load(filey)
            print("        Github")
            self.assertTrue("github" in content) 
            self.assertTrue(re.search("(\w+://)(.+@)*([\w\d\.]+)(:[\d]+){0,1}/*(.*)",content['github']) is not None)
            self.assertTrue(isinstance(content["github"],str))
            print("        Maintainers")
            self.assertTrue("maintainers" in content) 
            self.assertTrue(isinstance(content["maintainers"],list)) 
            for maintainer in content['maintainers']:
                self.assertTrue(isinstance(maintainer,dict))
                self.assertTrue("email" in maintainer)
                self.assertTrue("github" in maintainer)
                self.assertTrue("name" in maintainer)
                self.assertTrue(maintainer['github'].startswith('@'))
                self.assertTrue(re.search("^.+@.+[.]{1}.+$",maintainer['email']) is not None)

if __name__ == '__main__':
    unittest.main()
