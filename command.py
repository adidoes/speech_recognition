#! /usr/bin/python -u
# (Note: The -u disables buffering, as else we don't get Julius's output.)
#
# Command and Control Application for Julius
#
# How to use it:
#  julius -quiet -input mic -C julian.jconf 2>/dev/null | ./command.py
#
# Copyright (C) 2008, 2009 Siegfried-Angel Gevatter Pujals <rainct@ubuntu.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Supported commands:
#
# This file is provided as an example, and should be modified to suit
# your needs. As is, it only supports a few commands and executes them on
# either Rhythmbox or Banshee.

import sys
import os
import subprocess


class Commands:
	name = "Commands"
	
	commands = {
		'mute': ['amixer','set','Master','toggle'] #Hier sollte der command in der formatierung fuer subprocess.Popen() stehen
		}

	def parse(self,word):
		if word in self.commands:
			return self.commands[word]

class CommandAndControl:
	
	def __init__(self, file_object):
		
		self.cmd = Commands()
		
		startstring = 'sentence1: <s> '
		endstring = ' </s>'
		
		while 1:
			line = file_object.readline()
			if not line:
				break
			if 'missing phones' in line.lower():
				print 'Error: Missing phonemes for the used grammar file.'
				sys.exit(1)
			if line.startswith(startstring) and line.strip().endswith(endstring):
				print line
				self.parse(line.strip('\n')[len(startstring):-len(endstring)])
	
	def parse(self, line):
		# Parse the input
		params = [param.lower() for param in line.split() if param]
		if not '-q' in sys.argv and not '--quiet' in sys.argv:
			print 'Recognized input:', ' '.join(params).capitalize()
		
		# Execute the command, if recognized/supported
		print params
		command = self.cmd.parse(params[1])
		if command:
#			os.system(command)
			print "erkannt", command
			print subprocess.Popen(command,stdout=open("/dev/null"),stderr=open("/dev/null"))

if __name__ == '__main__':
	try:
		CommandAndControl(sys.stdin)
	except KeyboardInterrupt:
		sys.exit(1)
