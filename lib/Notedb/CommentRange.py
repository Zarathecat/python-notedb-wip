#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/CommentRange.pm

# This contains a tostr() function and some overloads. I suspect it should look
# very different in a python implementation. I believe it's used to establish
# which lines an inline comment should range over. So we have a startline, an
# endline, a startchar and an endchar.

class CommentRange(object):
    def __init__(self):
        self.starline = 1  # These all have getters but not setters; 'ro'.
        self.endline = 1
        self.startchar = 1
        self.endchar = 1
