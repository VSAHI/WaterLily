#!/usr/bin/python

#    routes.py
#    author: TuanNA
#    created date: 7/7/2015
#    ver 1.0
import imp

model_lib = imp.load_source('cores.model','..\libs\cores\model.py')
#from Project.libs.cores import router
#import Project.libs.cores.router as rt
def init_model():
    pass
def init_view(v):
    pass

model = init_model()
view = init_view("index.wp.py")
def indexController():
    print 'display view'
    return view
indexController()
model_lib.model('person')
