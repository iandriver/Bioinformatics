#!/bin/sh

# man.sh - `man` replacement for git bash on windows

# Dependencies (outside of git bash):
#  wget (http://users.ugent.be/~bpuype/wget/)

# TODO:
#  use sed to remove <head> & tags, convert HTML entities

# Notes:
#  `sed -r` = allows gnu regex extensions (like +)
#  `wget -qO -` = non-verbose output, returned file to stdout instead of file
#

if [ $# -eq 0 ] ; then
   echo "No command specified to get man page for"
   exit 1
fi

url="http://man.he.net/?section=all&topic="

#  The extra `+` at the end of the querystring doesn't hurt
for arg in $@ ; do
    url=$url$arg"+"
done

wget -qO - $url | sed 's/<[^>]*>//g' | less
