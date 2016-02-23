#!/usr/bin/env python
# coding=utf-8

import re

if __name__ == "__main__":
    print [e  for e in ['a-.','a-2','a3'] if re.search('a-.*', e) ] 
