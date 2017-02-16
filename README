# About NoteDB

NoteDB is a way of organising review content so that it is stored as git 
objects in the same git repo as the code, originally created by the people at
gerrit. https://gerrit.googlesource.com/homepage/+/md-pages/docs/Notedb.md

# This project

This is a WIP of a python NoteDB parser. It is a translation of the perl
code found at 

https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/?h=ripsum/spec&id=79408425ec9d443a83e3290d4295278f0a0b3198 

# Why

The goal is to make an API that can be used for code review, that allows teams
to keep the details of review in the same place as the code. This would mean
that code review could be decoupled from existing development suites, allowing
people to create custom UIs, clients, etc if wanted, and plug into other tools.
By using NoteDB specifically, we get multiple benefits, eg: review metadata is
preserved if the code is moved and offline code review is possible.


There is an existing implementation for both a NoteDB parser and a commandline
interface for code review, in perl, linked above. As python is a popular
language, we would like to make a python version, for interoperability with
existing tools written in python. Also, perl-notedb is
licensed under GPLv2, so this first draft is the same in order to use the same
structure by sharing the same libraries-- but in the future, with more
documentation on notedb available, it should be possible to create an
implementation compatible with the licensing for many existing projects that
cannot use GPLv2-licensed components.

# Resources

Richard Ipsum's notedb spec is available here:

https://git.gitano.org.uk/personal/richardipsum/perl-notedb.git/tree/notedb.md?h=ripsum/spec&id=79408425ec9d443a83e3290d4295278f0a0b3198
