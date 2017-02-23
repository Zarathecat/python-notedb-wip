#!/usr/bin/env
# GPLv2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/Metadata.pm 

# The original uses Carp for improved error-handling, and Git::Raw,
# so we probably need to import pygit2 here.

# it sets some properties for a metadata class, 'metadata_repo' (I'd guess 
# metadata about the repo rather than a repo of metadata, but hm.)
# 'revision', and 'change'. All these are read-writable.

# There's a BUILDARGS function, which checks if the metadata repo is
# defined, and errors if not. Then there's an if which I *think* tries
# to construct a metadata repo path based on the name of the repo,
# via 'open_repo' from utils. Still not sure how 'around' works; but
# the metadata repo path gets returned along with the rest, anyway.

# Then there are some stubs of functions, specifically:
# 'commit', 'commit_to_new_ref', 'remove_ref', 'on_load', 'get_ref_name',
# 'on_save', 'is_empty' ; these are all just `...`

# There's the `load` function, that I think finds a ref's repo based
# on its name. It says the metadata.revision will be the ref.target,
# then runs on_load, which I don't get yet, since that's a stub.

# Finally, there's a save function. I think this is the bit that
# actually writes built stuff, though need to check more closely.
