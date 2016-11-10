import os
import sys

def make_vocabulary_checklist():
    """ makes a vocabulary check list from the list provided 
    at the following url:
    
    https://fluent-forever.com/the-method/vocabulary/base-vocabulary-list/""" 
    
    corpus = []
    lines = open('data/vocabulary-625.txt').readlines()
    for l in lines:
        if 'Note' in l: continue
        print '\n##### {}\n'.format(l.split(':')[0])
        for ll in l.split(':')[1].strip().split(','):
            print '- [ ] {}'.format(ll.strip())
            corpus.append(ll.strip())
    
    #for c in corpus: print '- [ ] {}'.format(c)
    
    
if __name__ == '__main__':
    sys.exit(make_vocabulary_checklist())