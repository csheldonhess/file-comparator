# file-comparator
Compares files across two directories. 

I wrote this to make sure I was copying all of my music from one computer to another without missing any files.

As a one-time script (that I did a little cleanup on, because I am vain about what people see in my GitHub 😄), it is nothing fancy. 

## What it does

It asks the user for two directory paths, "original" and "copy." Then it iterates through each, prints the number of files in each to console, then runs a comparison in order to print a list of files that are in the original directory but not in the copy, then a list of files that are in the copy directory but not in the original. It's an imperfect but handy tool--and WAY faster than visually inspecting a large directory structure.

*Known issue*: It doesn't discriminate between "real" files and dotfiles (e.g. .DS_Store).

## How to run it on a Mac

Clone/Download the whole repository or just [compare.py](https://raw.githubusercontent.com/csheldonhess/file-comparator/master/compare.py), use a command line interface to navigate to the directory that contains compare.py, and type `python compare.py` to run the program. 

Make sure you know the full path to each directory (for instance: `\Users\username\Documents\Music\`), but don't worry too much; the program determine whether or not the path you enter is valid, and, if you give it invalid paths, it will just keep giving you more chances to get it right until you give it a valid path or ctrl-C out.

## Will it work on Windows or Linux?

 ¯\\_(ツ)_/¯ 

Probably? Let me know if you try it!
