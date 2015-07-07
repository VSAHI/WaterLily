#!/usr/bin/python

#    router.py
#    author: TuanNA
#    created date: 7/7/2015
#    ver 1.0

#f = open('../routes.py', 'r')

#for line in f:
#   print line,
#f.close()
import json
def route(rou,path,para):
    print rou
    print path
    if not para=="":
     #   print json.dumps(para, indent=4, separators=(',',':'))
        #data = json.loads(para)
        #print "param 1: " +data[0]
        #print "param 2: " + data[1]
        for k, v in para.items():
            print ": ".join((k, v))


