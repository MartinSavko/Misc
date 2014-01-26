#!/usr/bin/python

import commands
import os

directory = '/927bis/ccd/2013/Run4/2013-09-26/Vega/JQG3/5/MLE72'
print 'ls {directory}'.format(**{'directory': directory})

files = commands.getoutput('ls {directory}'.format(**{'directory': directory})).split('\n')

for f in files:
    fi = os.path.join(directory, f)
    print 'mv {orig} {new}'.format(**{'orig': fi, 'new': fi.replace('MLE72/MLE72', 'collect_0')})
    os.system('mv {orig} {new}'.format(**{'orig': fi, 'new': fi.replace('MLE72/MLE72', 'collect_0')}))