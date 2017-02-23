#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/CommitBuilder.pm

import pygit2 # we need the equivalent of git::raw::signature here, I think

# Just a class for the getters/setters of commit messages. They have a message,
# author and committer. That's it.

class CommitBuilder(object):
    def __init__(self):
        self.message = 'rw' # {'mode':'rw'}, one day
        self.author = 'rw' # inherits from signature
        self.committer = 'rw' #inherits from signature
