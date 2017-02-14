#!/usr/bin/env python

# wrapper on the pygit2 equivalent of 
# https://github.com/jacquesg/p5-Git-Raw/blob/master/lib/Git/Raw/Blob.pm
# goes here.
# based on the code at
# https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/BlobBuilder.pm
# which I don't fully understand yet.
# This should be changed into a class.

import repository from pygit2

class BlobBuilder(object):
    def __init__(self):
        self.repo = repository.BaseRepository()

    def create(self, buffer): #are $self, buffer in original, so just copying
        thing_to_create = (self, buffer) #next thing takes 1 param
        tree_or_blob = self.repo.whatever_to_tree_or_blob(thing_to_create)
        return tree_or_blob
