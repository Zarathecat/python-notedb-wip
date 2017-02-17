#!/usr/bin/env python

# wrapper on the pygit2 equivalent of 
# https://github.com/jacquesg/p5-Git-Raw/blob/master/lib/Git/Raw/Blob.pm
# goes here.
# based on the code at
# https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/BlobBuilder.pm
# I believe this is ultimately used to make comments, which are git notes;
# it's used in on_save in the original ChangeUpdate.pm
# pygit2 seems to use one
# function to make both trees and blobs, so we might not need a separate tree
# builder and blob builder.

import repository from pygit2

class BlobBuilder(object):
    def __init__(self):
        self.repo = {'mode': 'ro',
                     'required':1}

    def create(self, buffer):
        thing_to_create = (self, buffer) #whatever_to_tree_or_blob takes 1 param
        repo = repository.BaseRepository
        blob = repo.whatever_to_tree_or_blob(thing_to_create) #I should look
                                                              # at what original
                                                              # does with buffer
                                                              # here
        return blob
