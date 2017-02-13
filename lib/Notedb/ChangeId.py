#!/usr/bin/env python

# This is GPLv2; see COPYING
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/ChangeId.pm

class ChangeId(object):
    def __init__(self):
        # again, should probably be dicts?
        self.id = 'ro'
        self.is_uuid = 'ro'

    def get(self):
        # I think the original code returns the first index of the
        # the 'id'.
        return self.id[0]
