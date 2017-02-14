#!/usr/bin/env python

# GPL v2 (See COPYING)

# test code to print change info goes here

# these apparently should be the same, guess not for testing purposes
meta_repo = 'repo_goes_here'
content_repo = 'repo_goes_here'

change_list = ChangeList()
change_list.repo = meta_repo

change_ids = [ChangeId(), ] #I think this is an array rather than a tuple
change_ids.id = 1
change_ids.is_uuid = 0

change_notes = []
changes = []

for change_id in change_ids:
    change = Change()
    print 'Loading change ' + change_id.get()
    change_notes = ChangeNotes()
    change_notes.metadata_repo = meta_repo
    change_notes.changeid = change_id
    change_notes.change = change #hm, not sure about this
    change_notes.refprefix = 'refs/changes'

    change_notes.load()

    change_messages = change.changemsgs_bypatchsetid()
    print 'Change messages'
    for keys, values in change_messages.iteritems():
        print 'Patch-set: ' + str(k)
        # I think the next line just inserts some newlines, so leaving that out;
        # it does 'say "\n-80\n' , which I think is print two newlines (don't
        # know what the 80 refers to yet)
        for message in values: #guessing multiple messages per patch set
            print message

    comments = change_notes.comments

    print "Comments: "
    for sha, comment_map in comments.iteritems():
        value = comment_map.get_comment_list()
        # here there is an 'n' set equal to @v. but v is array and n is scalar.
        # wondering if that's a quick way to get the length or something
        i = 0 # Don't know what this is yet
        while i < v:                        # i < n in the original
            print "name=%d c%d" % (sha, i) + str(v[i]) #may not work
            i += 1

    reviewers = change.reviewers

    print "Reviewers: "
    for keys, values in reviewers.iteritems():
        print "key: %s    value:%s" % (keys, values) #don't know what look like

    topic = change.topic
    print "Topic: " + str(topic)

    status = change.status
    print "Status: " + str(status)

    print "Approvals: "
    approvals = change.approvals
    for keys, values in approvals.iteritems():
        for otherkeys, othervalues in values:
            print "approval: " + str(othervalues)

    print "PatchSets: "
    patchsets = change_notes.patchsets
    for keys, values in patchsets.iteritems():
        print "key: %s    value: %s" % (keys, values)

    print "Current patchest: " + change_notes.current_patchset
    print "Created on: " + change_notes.current_patchset.created_on
    print "RevId " + change_notes.current_patchset.revid
    print "Last updated on: " + change.last_updated_on
    print "Destination branch: " + change.destination_branch
    print "Subject: " + change.subject

    misc_author = UserIdentity()
    misc_author.author_name = 'Test user'
    misc_author.author_email = 'test@test'
    # I think 'cu' is 'user in change', so this says 'change user' but doesn't
    # change the user...
    change_user = change_notes.get_new_change_update(misc_author)
    change_user.load()

    change_user.patchset_id = change.current_patchset_id
    change_user.commit_subject = "Update patch set 2\n Patch set 2: \n \n(1 comment)"

    #well this bit needs work here...
    change_list = change_notes.comments."specific sha here".get_comment_list()

    #copied from original
    magicc = change_list[-1] #hm. dunno if this does python thing in perl yet
    print "magic_c: " + magicc
    # not sure about this syntax;
    # I think it's saying True or False based on if there's a comment,
    # but might be printing the comment
    print "Contains comment?: " + change_notes.contains_comment(magicc)

    # This kind of thing is all written out so I can follow it better;
    # should be tidied.

    patch_line_comment = PatchLineComment()
    patch_line_comment.revid = change_notes.current_patchest.revid #hm
    patch_line_comment.parent_uuid = magicc.parent.uuid
    patch_line_comment.patchset_id = change_user.patchset_id
    patch_line_comment.range = magicc.range
    # seems to find in original based
    #on string; we just use the author we created before for now
    patch_line_comment.author = misc_author
    #copied verbatim
    patch_line_comment.message = 'the other comment you need to merge in neatly'
    patch_line_comment.filename = 'GitUtils.py' #GitUtils.pm in original
    patch_line_comment.written_on = magicc.written_on

    patch_line_comment.uuid = hash_object(str(patch_line_comment)) # a guess

    print "Contains beef based comment?: " + change_notes.contains_comment(patch_line_comment)  #again, really don't know about this. not just because beef based.

    print 'inserting...'
    change_user.insert_comment(patch_line_comment)
    change_user.commit() #guessing function since last thing.
