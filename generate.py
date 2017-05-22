#!/bin/env python

'''

generate.py: Generate the base .json file to view valid experiments

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

from glob import glob
import os
import re
import sys
import json

from expfactory.validator import LibraryValidator
from expfactory.utils import write_json

here = os.getcwd()
experiments_base = "%s/experiments" %(here) 
experiments_url = "https://expfactory.github.io/experiments/experiments"
experiments = glob("%s/*" %experiments_base)

output_file = "%s/library.json" %(here)


validator = LibraryValidator()

final_set = []
for experiment in experiments:
   if validator.validate_all(experiment):
       with open(experiment) as filey:
           content = json.loads(filey.read())
       final_set.append(content)

write_json(final_set,output_file)
