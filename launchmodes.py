#!/usr/bin/env python3

"""
###################
launch Python programs with command lines and resusable launcher shceme classes;

"""

import sys, os
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python3'
pypath = sys.executable

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
		cmdline = cmdline.split()
		if os.fork() == 0:
			os.execvp(pypath, [pyfile] + cmdline)

class Start(LaunchMode):
	def run(self, cmdline):
		assert sys.platform[:3] == 'win'
		cmdline = fixWindowsPath(cmdline)
		os.startfile(cmdline)

class StartArgs(LaunchMode):
	"""
	for Windows only: args may require real start
	forward slashes are okay here
	"""
	def run (self, cmdline):
		assert sys.platform[:3] == 'win'
		os.system('start' + cmdline)

class Spawn(LaunchMode):
	"""
	run python in new process independent of caller
	for Windows or Unix; use 
	"""
	def run(self, cmdline):
		os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))

class Top_Level(LaunchMode):
	"""
	run in new window, same process
	tbd: requires GUI class info too
	"""
	def run(self, cmdline):
		assert False, 'Sorry - mode not yet implemented'

#
# pick a "best" launcher for this platform
# may need to specialize the choice elsewhere
#

if sys.platform[:3] == 'win':
	PortableLauncher = Spawn
else:
	PortableLauncher = Fork

class QuietPortableLauncher(PortableLauncher):
	def announce(self, text):
		pass

def selftest():
	file = 'echo.py'
	input('default mode....')
	launcher = PortableLauncher(file, file)
	launcher()

	input('system mode....')
	System(file, file)()

	if sys.platform[:3] == 'win':
		input('DOS start mode...')
		StartArgs(file, file)()

if __name__ == ' __main__': selftest()
