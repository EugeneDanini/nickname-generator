#!/usr/bin/env python

import sys
import nickname_generator

try:
    locale = sys.argv[1]
except IndexError:
    locale = None

print(nickname_generator.generate(locale))
exit(0)
