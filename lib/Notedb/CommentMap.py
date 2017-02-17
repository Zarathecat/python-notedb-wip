#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/CommentMap.pm

# This preserves the order in which comments are added.
# I think there is a separate class for this here because the order of comments
# in a git note can vary depending on the client used, but a parser should
# display them in the same order to ensure  minimal diffs.
# see: https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/notedb.md?h=ripsum/spec#n197

# So, multiple patchlinecomments are stored in the same
# blob, which can lead to merge conflicts. (gerrit avoids this by
# being centralised, so that comments are not added in a distributed way
# at the same time, leading to conflicts. it could be worth looking at how
# gertty handles this; this issue is seen as outside the scope of notedb)
# 
# CommentMap has an 'order' property to keep the order in which comments are
# added. When a comment is added, the comment's uuid is used to establish
# where in the order it should be. I don't get exactly how this works yet. 

# the original uses Carp for error-handling
