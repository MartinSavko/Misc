#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Get the full story from the web of stories http://www.webofstories.com/play'''

import optparse
import pickle 
import urllib2

def getSegment(page, beginning, ending):
    segment = page[page.index(beginning) + len(beginning):]
    segment = segment[:segment.index(ending)]
    segment = segment.strip()
    return segment
    

def getNumberOfSegements(page):
    b1 = 'activatePaginationLinks(true'
    e1 = ');'
    s1 = getSegment(page, b1, e1)
    number = int(s1.split(',')[-1])
    return number
    

def getTitle(page):
    beginning = '<meta property="og:title" content="'
    ending = '" />'
    title = getSegment(page, beginning, ending)
    return title
    

def getTranscript(page):
    beginning = '<div id="transcript-en" class="transcriptText">'
    ending = '</div>'
    transcript = getSegment(page, beginning, ending)
    return transcript
    
    
def getPage(url):
    response = urllib2.urlopen(url)
    page = response.read()
    response.close()
    return page

    
def storeData(data, filename):
    f = open(filename, 'w')
    pickle.dump(data, f)
    f.close()
    

def getFullStory(name):
    try:
        f = open(name + '_story.pck')
        story = pickle.load(f)
    except IOError:
        baseUrl = 'http://www.webofstories.com/play/' + name
        story = {}
        story['name'] = name
        
        firstPage = getPage(baseUrl + '/1')
        numberOfSegments = getNumberOfSegements(firstPage)
        story['numberOfSegments'] = numberOfSegments

        for n in range(1, numberOfSegments + 1):
            url = baseUrl + '/' + str(n)
            try:
                page = story[n]['page']
            except KeyError:
                page = getPage(url)
            title = getTitle(page)
            transcript = getTranscript(page)
            story[n] = {'title': title,
                        'transcript': transcript,
                        'page': page}
        storeData(story, name + '_story.pck')
    return story
    

def writeDown(story):
    f = open(story['name'] + '.txt', 'w')
    for n in range(1, story['numberOfSegments'] + 1):
        f.write(story[n]['title'] + 2*'\n')
        f.write(story[n]['transcript'] + 4*'\n')
    f.close()
    

def writeDownHtml(story):
    name = story['name']
    f = open( name + '.html', 'w')
    f.write('<html>\n')
    f.write('\t<head>\n')
    f.write(2*'\t' + '<title>Story of ' + ' '.join([ n.capitalize() for n in name.split('.')]) + ' from the web of stories</title>\n')
    f.write(2*'\t' + '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
    f.write('\t</head>\n')
    f.write('\t<body>\n')
    for n in range(1, story['numberOfSegments'] + 1):
        f.write(2*'\t' + '<h3>' + story[n]['title'] + '</h3>' + 2*'\n')
        f.write(2*'\t' + story[n]['transcript'] + 4*'\n')
    f.write('\t</body>\n')
    f.write('</html>\n')
    f.close()
    
    
usage = 'Get the full story from the web of stories http://www.webofstories.com/play'
parser = optparse.OptionParser(usage = usage)

parser.add_option('-n', '--name', default='marvin.minsky', type=str, help='name of the person whose full story we are interested in (default: %default)')

#parser.add_option('-h', '--name', default='marvin.minsky', type=str, help='name of the person whose full story we are interested in (default: %default)')

options, args = parser.parse_args()

print options, args

story = getFullStory(options.name)

writeDown(story)
writeDownHtml(story)
