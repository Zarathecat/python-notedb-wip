#!/usr/bin/env python

# This is GPLv2; see COPYING
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/ChangeId.pm

# In the original, it looks like this just gets the id of the thing passed to
# it. Which happens to be a change. and a change is a collection of at least
# one patchset. A patchset = patchlinecomment(s) and a commit. So, collections
# of patchsets, or 'changes', wind up with IDs.

class ChangeId(object):
    def __init__(self, id, is_uuid):
        self.id = {'mode':'ro', 'required':1}
        self.is_uuid = {'mode':'ro', 'required':1}

    def get(self):
        return self.id
