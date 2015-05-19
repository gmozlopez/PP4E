"""
###################
launch Python programs with command lines and resusable launcher shceme classes;

"""

import sys, os
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pypath = sys.excecutable

def fixWindowsPath(cmdline):
    splitline = cmdline.lstrip().split(' ')
    fixedpath = os.path.normpath(splitline[0])
    return ' '.join([fixedpath] + splitline[1:])

class LaunchMode:
    def __init__(self, label, command):
        self.what  = label
        self.where = command
    def __call__(self):
        self.announce(self.what)
        self.run(self.where)
    def announce(self, text):
        print(text)
    def run(self,cmdline):
        assert False, 'run must be defined'

class System(LaunchMode):
    def run(self,cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.system('%s %s' % (pypath, cmdline))

class Popen(LaunchMode):
    def run(self,cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pypath + ' ' + cmdline)

class Fork(LaunchMode):
	def run(self, cmdline):
		assert hasattr(os, 'fork')