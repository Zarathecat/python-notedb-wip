#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/NotedbRepo.pm

import pygit2 # this uses git::Raw::Repository in the original

# this makes a NotedbRepo class with a ro `repo` attribute, matching
# the git::raw::repository type in the original. and is required
# (I think that's used in validate_kwargs in utils, but it may be
# something totally different and correspond to some python
# @property thing, so should check)

# There's a function a lot like the one in Metadata, BUILDARGS,
# that opens a repo based on the repo given via the git::raw::repository
# function, and returns its path as part of the class. And
# there's an `insert` function; this returns
# self.repo.head.name if given a valid Change, otherwise returns undef.
# I'm not surewhy it's called 'insert', yet; it doesn't seem to insert
# anything. There are other subroutines in toher packages called 'insert'
# and this one doesn't seem to be called anywhere.
