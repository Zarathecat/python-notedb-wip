#!/usr/bin/env python
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/Commit.pm

# This is described as a wrapper around Git::Raw::Commit, so we need the pygit2
# equivalent.

# it sets the raw commit property to read only. Then there's a rtrim function
# to strip something, but I don't know what it's stripping yet (whatever \s
# expands to in perl, I guess). It's the thing that turns the raw commit into
# the commit message in get_footer_lines, anyway.

# There's a function to check if something
# passed is a footer, based on whether it matches a regexp; I think the
# regexp checks if it's a string with alphanumeric charas followed by a
# colon.

# That seems like that would give the key of the footer. But wait!
# get_footer_lines reverses the relevant line of the commit, so that the
# footer would actualy be at the start of the string. These are then
# re-reversed to their original order.

# There's a function to get the commit message from raw_commit, and I think
# that cuts out footer lines. Then there are simple functions to get
# id, author, committer, message, parents and time (just raw_commit.foo for
# each of those). The raw commit is set in ChangeNotesParser, passed via
# parse_single_footer. I think it originally comes from walker.

push @{$self->{changemsgs_bypatchsetid}{$ps_id}}, $commit->get_commit_message;

would become commit = changemsgs_bypatchsetid(ps_id)
             get_commit_message(commit)

but I need to check how the perl `push` works when I get off this plane...
