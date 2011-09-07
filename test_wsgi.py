import sys
import win32traceutil
traceon = 1

#import os
# Change working directory so relative paths (and template lookup) work again
#os.chdir(r"C:\\Inetpub\\wwwroot\\kotodo")

import bottle
from kotodo import ret_kotoapp
# Do NOT use bottle.run() with mod_wsgi
application = ret_kotoapp()

import isapi_wsgi
# The entry points for the ISAPI extension.
def __ExtensionFactory__():
    # can also be isapi_wsgi.ISAPISimpleHandler
    # return isapi_wsgi.ISAPIThreadPoolHandler(application)
    return isapi_wsgi.ISAPIThreadPoolHandler(application)

if __name__=='__main__':
    # If run from the command-line, install ourselves.
    from isapi.install import *
    params = ISAPIParameters()
    # Setup the virtual directories - this is a list of directories our
    # extension uses - in this case only 1.
    # Each extension has a "script map" - this is the mapping of ISAPI
    # extensions.
    sm = [
        ScriptMapParams(Extension="*", Flags=0)
    ]
    # To serve from root, just set Name="/"
    vd = VirtualDirParameters(Name="/",
                              Description = "ISAPI-WSGI Kotodo",
                              ScriptMaps = sm,
                              ScriptMapUpdate = "replace"
                              )
    params.VirtualDirs = [vd]
    HandleCommandLine(params)