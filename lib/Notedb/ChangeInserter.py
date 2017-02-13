#!/usr/bin/env python
# GPL v2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/ChangeInserter.pm
# this is mainly pass statements since the code is pretty dense

class ChangeInserter(object):
    def __init__(self):
        self.content_repo = 'ro'
        self.id_type = 'ro'
        self.id_generator = 'ro'
        self.refprefix = 'ro'
        
        self.next_id = 'ro'

    def build(self):
        # not sure if we just want the first thing in the id or if
        # removing the element from it is also important.
        # the perl uses `shift` here
        selected_id_type = id_type.pop(0)
        if selected_id_type == 'UUID':
            next_id.pop(0) = make_uuid_change_id #undefined
            return #yeah no idea what's going on here yet.
        elif selected_type == 'callback':
            next_id.pop(0) = THERE IS AN ANON FUNCTION IDK
            return

        _next_id.pop(0) = ANOTHER ANON FUNCTION

    def next_integer_change_id:
        pass

    def make_uuid_change_id:
        pass

    def insert:
        pass
