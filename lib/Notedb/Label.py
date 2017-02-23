#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/Label.pm

# This parses Labels, which are used to track (dis)approvals in notedb, eg:
# Label: Code-Review=+1 . It makes a class with two properties, a key and
# a value. The key is the bit between 'Label:' and the '='. The value is
# the bit after the =. so `key: Code-Review   , value: +1`
# Then there is a from_string function which actually works out which
# bit of a passed string is the key and value,in a case where:
# a) there is a key and value
# b) there is a key but no value
# c) the string is invalid

# Once it's got the key and value, it sets them as properties of the class.
# Nice and straightforward. :)
