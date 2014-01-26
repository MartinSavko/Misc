#!/usr/bin/python

'''Check detector distance'''

import commands
import os
import numpy

import matplotlib.pyplot as plt
import numpy as np


#dirtocheck = '/927bis/ccd/2013/Run*/2013-*/*'
dirtocheck = '/927bis/ccd/2013/Run3/2013-05-21/Commissioning/BCT/'

pattern = 'collect'

look = 'find %s -wholename "*process/xds_process_*/CORRECT.LP"' % dirtocheck

lookin = commands.getoutput(look).split('\n')

lref = 'grep "CRYSTAL TO DETECTOR DISTANCE (mm)" %s/CORRECT.LP | cut -d ")" -f 2'
linp = 'grep "DETECTOR_DISTANCE" %s/XDS.INP | cut -d "=" -f 2'

currentdir = os.getcwd()

diffs = []
distances = []
refined = []

print 'lookin', lookin
for l in lookin:
    l = os.path.dirname(l)
    print 'l', l
    try:
        inp = float(commands.getoutput(linp % l))
        ref = float(commands.getoutput(lref % l))
        difference = inp - ref
        print 'for input distance %s the difference is %s' % (inp, difference) 
        if -.5 < difference < 1.5:
            diffs.append(inp - ref)
        distances.append(inp)
        refined.append(ref)
    except:
        pass
    
d = numpy.array(diffs)
print 'differences'
print d


c = list(d)
print 'list representation of differences'
print c
m = c.index(d.max())
print 'The maximum difference occured for the distance %s (the difference was %s), the average difference is %s' % (distances[m], diffs[m], d.mean())


hist, bins = np.histogram(d, 7)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()