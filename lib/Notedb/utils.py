#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/utils.pm

# The original imports Carp, a core module for fancy exception handling.

import pygit2 # git::raw is imported in the original

# function to check you've supplied the kwargs you need to supply
def validate_kwargs(kwargs_ref, required):
    for thing in required:
        if thing not in kwargs_ref:
            print 'No %s provided' % thing # this uses Carp's 'confess' to die
                                           # not sure of exact equivalent yet
            return 1                       # so just returning an error code

# I think this currently hashes the object by setting an 'object' variable,
# printing it and then piping the printed thing into git hash-object. It
# then saves the result of that command to a variable, cuts a newline(?) off
# and returns that variable. this approach is listed as a FIXME in the original
def hash_object(object):
    hashed_object = 'git hash-object --stdin' # command to hash object; should
                                              # be passed to a lib that'd
                                              # actually run it
    print hashed_object
    # I think the next thing here, chomp, strips the newline from the printed 
    # hashed_object. I haven't coded that since I agree we should do this
    # differently
    return hashed_object

def open_repo(path):
    return repository.open(path) # uses git:raw:repository, so a pygit2 thing
