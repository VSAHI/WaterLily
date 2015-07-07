#!/usr/bin/python

#    routes.py
#    author: TuanNA
#    created date: 7/7/2015
#    ver 1.0

import libs.cores.router as rt
rt.route("index","index",{})
rt.route("user/","user/index",{"id":"number","page":"number"})
rt.route("data/product","data/product",{"from":"number","to":"number"})
