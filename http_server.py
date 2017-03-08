#!python
# -*- coding: utf-8 -*-
import sys
reload(sys)
exec("sys.setdefaultencoding('utf-8')")
assert sys.getdefaultencoding().lower() == "utf-8"

import cherrypy;
import os, json;
import time;

def get_abs_dir(relative_dir):
    dir = os.path.abspath(os.path.curdir);
    abs_path = os.path.join(dir, relative_dir);
    return abs_path;

def enable_crossdomain():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*";
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, POST, HEAD, PUT, DELETE";

    # generate allow headers for crossdomain.
    allow_headers = ["Cache-Control", "X-Proxy-Authorization", "X-Requested-With", "Content-Type"];
    cherrypy.response.headers["Access-Control-Allow-Headers"] = ",".join(allow_headers);

class Root(object):
    exposed = True
    def __init__(self):
        pass;

    def GET(self):
        enable_crossdomain();
        raise cherrypy.HTTPRedirect("bravo-player-ng/BravoPlayer_Main/bin-debug/Player.html");

if __name__ != "__main__":
    print "system+start start error";
    raise Exception("not support");

# set cherrypy params
boot_params = {
    'global': {
        # cherrypy will wait timeout when client is alive
        # @see: ServerAdapter.stop at cherrypy.process.servers.py
        # @remark: float is ok, for example 0.1, got a warning for the
        # cherrypy._cpserver.shutdown_timeout is int.
        'server.shutdown_timeout': 1,
        'server.socket_host': "0.0.0.0",
        'server.socket_port': 80,
        'tools.staticdir.on': True,
        'tools.encode.on': True,
        'tools.encode.encoding': "utf-8"
    },
    '/': {
        'tools.staticdir.dir': get_abs_dir('./'),
        'tools.staticdir.index': "index.html"
    }
}

print "listen at %s:%s"%(
    "0.0.0.0",
    80
);

cherrypy.quickstart(Root(), "/", boot_params);
