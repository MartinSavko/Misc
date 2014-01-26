#!/usr/bin/python

import commands
import os
import optparse

usage = 'Rename files matching patern <files_to_rename> substituting <to_replace> by <replace_by>.'

parser = optparse.OptionParser(usage=usage)

parser.add_option('-f', '--files', type=str, default='/927bis/ccd/2013/Run5/2013-11-09/Vega/JQGH/1/test_4_????.img', help='files to replace')
parser.add_option('-t', '--to_replace', type=str, default='test_4_', help='string in the filenames to be replaced')
parser.add_option('-b', '--replace_by', type=str, default='collect_1_', help='string to replace by')

options, args = parser.parse_args()
print 'options', options
print 'args', args

files_to_rename = options.files #  "/927bis/ccd/2013/Run5/2013-11-10/Vega/20131106MLE2/2/test_2_*" #options.files #'/927bis/ccd/2013/Run5/2013-11-09/Vega/JQGH/1/test_4_????.img'

to_replace = options.to_replace #'test_4_'
replace_by = options.replace_by #'collect_1_'

files = commands.getoutput('ls %s' % files_to_rename).split('\n')

print files

for fil in files:
    com = 'mv %s %s' % (fil, fil.replace(to_replace, replace_by))
    print com
    os.system(com)
