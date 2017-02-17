#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/Timestamp.pm

import time #original uses date::language, I think these let us do the same
import locale

class Timestamp(object):
    def __init__(self):
        self.time_t = {'mode': 'ro', 'required':1}
        self.zone = {'mode': 'ro', 'required':1}

# More from the 'around' modifier. lines 15-26 are TODO.

    def to_string(self):
        # ripsum's note copied from the original:
        # 'To be compliant with gerrit we should be outputting
        # a string such as
        # "Fri Jan 29 11:50:09 2016 +0000"'
        lang = 'something_with_time_and_locale'

#Then some perl-specifics follow, string-equality-overloading
