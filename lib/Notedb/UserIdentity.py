#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/utils.pm

class UserIdentity(object):
    def __init__(self):
        self.author_name = {'mode':'ro', 'required':1} #maybe True
        self.author_email = {'mode':'ro', 'required':1}

    def from_git_raw_signature(self, sig):
        name = sig.name
        email = sig.email
        raw_sig = self.from_string("%s <%s>" % (name, email))
        return raw_sig

    def from_string(self, user): #idk what s is yet
        name = ''
        email = ''

    if user == 'a thing satisfying regexp': #REGEXP HERE IN ORIGINAL
        name = 'first bit checked in regexp' 
        email = 'second bit checked in regexp'
    else:
        raise exception 'Failed to parse UserIdentity from string: ' + user

    return UserIdentity(author_name = name, author_email = email)

    def to_string(self):
        name = self.author_name
        email = self.author_email
        user_string = str(name) + str(email)#these may be strings anyway for us
        return user_string

    # There are a couple of other things that look specific to perl about
    # overriding string equality; I've left them for now.
