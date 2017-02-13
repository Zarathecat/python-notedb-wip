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

    def create():
        ONEPARAMETER = (thing, otherthing) #don't know what this is yet
        tree_or_blob = repo.whatever_to_tree_or_blob(ONEPARAMETER)
        return tree_or_blob
