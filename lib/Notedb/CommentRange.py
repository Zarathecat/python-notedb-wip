#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/CommentRange.pm

# This contains a tostr() function and some overloads. I suspect it should look
# very different in a python implementation. I'm not sure if it's used to see
# what lines in a note are for a specific comment, or if it's used to see what
# lines in a patch a comment ranges over for inline comments.
# Anyway, if nothing else, I'm fairly confident we have a startline, an
# endline, a startchar and an endchar.

class CommentRange(object):
    def __init__(self):
        self.starline = 1  # These all have getters but not setters; 'ro'.
        self.endline = 1
        self.startchar = 1
        self.endchar = 1
