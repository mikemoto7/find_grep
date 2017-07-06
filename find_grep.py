#!/usr/bin/env python

"""
%(scriptName)s Runstring:

%(scriptName)s [--start_dir dirpath] [--ignore_case] --filename_mask ".*\.py$" --search_string some_regex_string

If you rename a variable, a function, a module/package, or a script/program, you may want to know what other files use the old name so you can update them to the new name.

This script is the Python version of the Linux find/grep command combination.  It does not do everything find/grep does, but it will do a basic find/grep search.  Search matches will be displayed to your screen.

If you have a lot of files to search through but infrequent matches, you may not see any screen output for several minutes.  Use the following to see what files are currently being found and searched:

   <ctrl-c> = Monitor mode:  Toggle displaying the names of all files whether search_string was found in them or not.  These monitor-mode filenames will have a '#' in front of them to distinguish them from displayed search match filenames.

TBD:

find/grep/replace

%(scriptName)s [--start_dir dirpath] [--ignore_case] --filename_mask ".*\.py$" --search_string some_regex_string --replacement_string a_non-regex_string


"""

import os, sys, re
import getopt

scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))
scriptDir_lib = scriptDir + '/lib'
sys.path.append(scriptDir_lib)

sys.path.append("lib")

from dir_tree import dir_tree
from batch_edit_one_file import replace_string, grep_string

import command_list

scriptName = os.path.basename(__file__).replace('.pyc', '.py')

#==============================================

def usage():
    print(__doc__ % {'scriptName': scriptName, })
    sys.exit(1)

#==============================================

def find_grep(options):
    if options.get('--replacement_string', False) == True:
       rc, files_found = dir_tree(start_dir=options.get('--start_dir', '.'), filename_mask=options.get('--filename_mask', '.*'), func=replace_string, options=options.get('--print_all_filenames', ''), search_string=options.get('--search_string', 'BAD_SEARCH_STRING'), replacement_string=options.get('--replacement_string', 'BAD_REPLACEMENT_STRING.'))
    else:
       rc, files_found = dir_tree(start_dir=options.get('--start_dir', '.'), filename_mask=options.get('--filename_mask', '.*'), func=grep_string, options=options, search_string=options.get('--search_string', 'BAD_SEARCH_STRING'))



#==============================================

if __name__ == '__main__':

    command_list.command_list(argv=sys.argv, your_scripts_help_function=[usage, 'return'])

    if len(sys.argv) == 1:
        print(__doc__ % {'scriptName': scriptName, })
        sys.exit(1)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["start_dir=", "filename_mask=", "search_string=", "replacement_string=", "print_all_filenames", "ignore_case"])
    except:
        print("ERROR: Unrecognized runstring option.")
        usage()

    options = {}

    for opt, arg in opts:
        any_option = True
        if opt == "--start_dir":
            options[opt] = arg
        elif opt == "--filename_mask":
            options[opt] = arg
        elif opt == "--search_string":
            options[opt] = arg
        elif opt == "--replacement_string":
            options[opt] = arg
        elif opt == "--print_all_filenames":
            options[opt] = opt 
        elif opt == "--ignore_case":
            options[opt] = True
        else:
            print("ERROR: Unrecognized runstring option: " + opt)
            usage()


    find_grep(options)


