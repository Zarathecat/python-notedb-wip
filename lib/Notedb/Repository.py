#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/Repository.pm

class Repository(object):
    def __init__(self):
        self.repo = 'ro' #probably should be self.repo= {'mode':'ro'}
