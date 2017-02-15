#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/PatchSet.pm

class PatchSet(object):
    def __init__(self):
        self.patchset_id = 'rw' #again, should probably be {'mode':'rw'}

        self.subject = 'rw'
        self.message = 'rw'

        self.author = 'rw' #this also inherits things from notedb useridentity
        self.committer = 'rw' #also inherits from there

        self.revid = 'rw'
        self.parents = 'rw'

        # according to original, gerrit seems to assume GMT. I would guess it
        # assumes UTC which happens to be the same.
        self.created_on = 'ro'

    # This has an around modifier, which I think is a way of passing the
    # function used to call this function to this function
    # so that's todo...

