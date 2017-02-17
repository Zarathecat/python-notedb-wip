#!/usr/bin/env python

#GPLv2 (see COPYING)

# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/ChangeNoteUtil.pm

# This defines some footers that are stored at the end of the commit message,
# gets a refname from some specified ref_prefix and change_id,
# and finds the change id for a specified ref(name?)

FOOTER_BRANCH = 'Branch'
FOOTER_COMMIT = 'Commit'
FOOTER_PATCH_SET = 'Patch-set'
FOOTER_STATUS = 'Status'
FOOTER_SUBJECT= 'Subject'
FOOTER_TOPIC = 'Topic'
FOOTER_LABEL = 'Label'
FOOTER_REMOVED = 'Removed'
# original says this is not a complete set of footers. so repeating that here
# so it doesn't get forgotten.

class ChangeNoteUtil(object):
    def __init__(self):
        pass

    def change_ref_name(class, change_id, ref_prefix):
        refname = []
    
        # The code here is different from gerrit's notedb;
        # not sure if we want it exactly the same or not
        # for now I've left this.
        prefix = ref_prefix
    
    def change_id(class, change_meta_ref):
         if change_meta_ref = '': # SHOULD BE REGEXP HALP
             change_id = ChangeId()
             bit_of_thing_matched_in_brackets_in_regexp = 'todo'
             # guess 'looks_like_sha' is perl's 'looks_like_number',
             # that has been extended somehow
             if:
                 looks_like_sha(bit_of_thing_matched_in_brackets_in_regexp)
                 is_uuid = True
                 change_id.id = bit_of_thing_matched_in_brackets_in_regexp
                 return change_id
            return None #this is return undef in original
