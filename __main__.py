#! /usr/bin/python
# vim: set fileencoding=utf-8 :
# XXXXXXXX (Python script) -- 
#
# Version:   
# Copyright: (c)2016 Alastair Irvine <alastair@plug.org.au>
# Keywords:  
# Notice:    
# Licence:   This file is released under the GNU General Public License
#
'''Description:
  
Usage: 
Options:
  
'''
# Licence details:
#     This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 2 of the License, or (at
#     your option) any later version.
#
#     See http://www.gnu.org/licenses/gpl-2.0.html for more information.
#
#     You can find the complete text of the GPLv2 in the file
#     /usr/share/common-licenses/GPL-2 on Debian systems.
#     Or see the file COPYING in the same directory as this program.
#
#
# TO-DO:

import sys
import getopt
from roman import generate
from RomanNumeral import RomanNumeral



## operators = { '-': subtract, '+': add }

a = RomanNumeral(sys.argv[1]).get()
b = RomanNumeral(sys.argv[2]).get()

print generate(a + b)
