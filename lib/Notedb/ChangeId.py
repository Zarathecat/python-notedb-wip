#!/usr/bin/env python

# This is GPLv2; see COPYING
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/ChangeId.pm

class ChangeId(object):
    def __init__(self, id, is_uuid):
        # again, should probably be dicts?
        self.id = 'ro'
        self.is_uuid = 'ro'

    def get(self):
        return self.id
