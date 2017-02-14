#!/usr/bin/env python
# GPL v2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/ChangeInserter.pm
# import ChangeId, ChangeList, Signature # these should really come from the
#                                        # shared notedb package instead
# this is mainly pass statements since the code is pretty dense

class ChangeInserter(object):
    def __init__(self):
        self.content_repo = 'ro'
        self.id_type = 'ro'
        self.id_generator = 'ro'
        self.refprefix = 'ro'
        
        self.next_id = 'ro'

    def build(self):
        # TURNS OUT I HAD THIS TOTALLY BACKWARDS; $self = shift
        # refers to the current object...
        new_id_type = self.id_type
        if new_id_type == 'UUID':
            self.next_id = make_uuid_change_id #defined below... one day.
            return self.next_id
        elif selected_type == 'callback':
            next_change = ChangeId()
            new_id = # something with id_generator...
            next_change.id = # will be the new id...
            next_change.is_uuid = '1'
            return self.next_id

        self.next_id = next_integer_change_id(self)

    def next_integer_change_id(self):
        changelist = ChangeList()
        changelist.repo = self.metadata_repo.path
        num_of_changes = changelist.repo.changes # really not sure I get this


    def make_uuid_change_id(self):
        head = self.content_repo.head.target #maybe this should be like
                          # self.content_repo[head][target] ...
        tree = head.tree.id #etc
        author = Signature()
        author.signature = head.author
        committer = Signature()
        commit.signature = head.committer
        parents = head.parents #each parent, joined on a newline? idk
                               #how perl's map works yet so not sure here
        obj = 'EOF' # yeah, really don't know about this. I think this is
                    # inserted at end so that this can be used to write
                    # to a file as-is, so we'd do it a bit differently
                    # in python anyway. maybe this is meant to be the
                    # null byte for the end of the header?

        new_change_id = ChangeId()
        new_change_id.id = utils.hash_object(obj) # utils is a class from
                                                  # our package. This
                                                  # line does not look ok
                                                  # to me at all...
        

    def insert:
        pass
