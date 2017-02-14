#!/usr/bin/env python
# GPL v2 (see COPYING)
# based on https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/lib/Notedb/ChangeInserter.pm
# import ChangeId, ChangeList, Signature # these should really come from the
#                                        # shared notedb package instead
import pygit2

# I think this acts as a decorator on the Metadata class
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
        changelist.repo = self.metadata_repo.path #this obj doesn't have a 
                                                  # metadata repo, so must get
                                                  # it from class it decorates.
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
        obj = 'EOF' # this is inserted at end so that this can be used to write
                    # to a file as-is, so we'd do it a bit differently
                    # in python anyway (probably just call this content from
                    # a file-writing function. it's known as a 'here document'
                    # in perl)

        new_change_id = ChangeId()
        new_change_id.id = utils.hash_object(obj) # utils is a class from
                                                  # our package. This
                                                  # line does not look ok
                                                  # to me at all...
        

    def insert(self, subject, commit_subject, destination_branch,
               author, revid):
        # I think the first 'validate'
        # line here checks we have been passed the right
        # sort of data. So we could still check the author satisfies the
        # regexp and the revid is 0, but otherwise that's different here
        self.content_repo = open_repo(self.content_repo) #open_repo from utils
        if revid: # in perl there's the // operator for definedness, so this
                  # is my attempt at replicating that here
            revid = self.content_repo.lookup(revid) #hm
        commit_obj = self.content_repo.lookup(revid)

        # the below is 'die' in perl
        if commit object is not 'pygit2_version_of_git_raw_commit_goes_here':
            try:
                raise exception
            except exception as invalid_commit_object:
                print 'Object at %d is not a commit' % revid

        parents = commit_obj.parents

        change = Change()
        change.changeid = self.next_id() #hm
        change_notes = ChangeNotes()
        change_notes.metadata_repo = self.metadata_repo.path
        change_notes.content_repo = self.content_repo
        change_notes.changeid = change.changeid
        change_notes.change = change
        change_notes.refprefix = self.refprefix

        author = UserIdentity.from_string(author)

        update = change_notes.get_new_change_update(author)#should make a class

        update.status = Change.statuses[NEW]
        update.subject = subject
        update.commit_subject = commit_subject
        update.destination_branch = destination_branch
        update.topic = topic
        update.author = author
        update.set_commit = revid #changenotes calls changeupdate
                                  # which has set_commit, etc
        update.patchset_id = 1 # this is patchset_id(1) so should check that's
                               # actually saying it's equal to 1
        update.commit # I don't know why this is on its own in the original
                      # am keeping it here so I remember to check that
        return update
