#!/usr/bin/env python

# GPL v2 (See COPYING)

# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/Change.pm

class Change(object):
    statuses = { 
                      NEW = 'new',
                      DRAFT = 'draft'
                      MERGED = 'merged'
                      ABANDONED = 'abandoned'
               }

    def __init__(self):
        # I think these should be key-value pairs but not sure
        # the perl code uses Mouse to set an accessor, eg
        # a read only accessor, for each of these. As you can
        # tell, I just know the words 'read only accessor' and
        # cannot tell you what this looks like. so right now
        # I'm conceptualising it as:
        # 'each of these attributes includes
        # an 'access' property, which might be 'rw' or 'ro',
        # and will be taken as a parameter elsewhere.
        self.changeid = 'rw'
        self.owner = 'rw'
        self.timestamp = 'rw'
        self.last_updated_on = 'rw'
        self.status = 'rw'
        self.destination_branch = 'ro'
        self.subject = 'rw'
        self.current_patchset_id = 'rw'
        self.topic = 'rw'
        self.reviewers = 'ro'
        self.changemsgs_bypatchsetid = 'ro'

    

    def is_new(self):
        self.status = statuses[NEW]
        return self.status
    def is_abandoned(self):
        self.status = statuses[ABANDONED]
        return self.status
    def is_draft(self):
        self.status = statuses[DRAFT]
        return self.status
    def is_merged():
        self.status = statuses[MERGED]
        return self.status

# the original script returns 1 if nothing else returns so that an error
# is returned; should have an equivalent.
