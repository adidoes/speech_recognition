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

globalPopenList = []

class Commands:
	name = "Commands"
	ids = ['lux','lacer','alexia','pi']
	
	def RunningMusic(self,player):
		psOut = subprocess.check_output(['ps','aux'])
		psOut = psOut.split()
		i=0
		while i<len(psOut):
			psOut[i] = psOut[i].strip().lower()
			i+=1
		for each in psOut:
			if each.find(player) >= 0:
				print each,player
		if player in psOut:
			ret= True
		else:
			ret= False
			
		return ret

	def parse(self,word):
		if word[0] == 'error':
			return None
		if str(word[0]) in self.ids:
#MUTE
			if 'mute' in word:
				return ['amixer','set','Master','toggle']

# VOLUME
			if 'volume' in word:
				if 'up' in word:
					return ['amixer','set','Master','5%+']
				if 'down' in word:
					return ['amixer','set','Master','5%-']

				if 'one' in word:
					if not 'hundred' in word:
						return ['amixer','set','Master','1%']
				
				if 'two' in word:
					return ['amixer','set','Master','2%']

				if 'three' in word:
					return ['amixer','set','Master','3%']

				if 'four' in word:
					return ['amixer','set','Master','4%']

				if 'five' in word:
					if not 'twenty' in word and not 'thirty' in word and not 'fourty' in word and not 'fifty' in word and not 'sixty' in word and not 'seventy' in word and not 'eighty' in word and not 'ninety' in word:
						return ['amixer','set','Master','5%']

				if 'ten' in word:
					return ['amixer','set','Master','10%']

				if 'fifteen' in word:
					return ['amixer','set','Master','15%']

				if 'twenty' in word:
					if 'five' in word:
						return ['amixer','set','Master','25%']
					else:
						return ['amixer','set','Master','20%']

				if 'thirty' in word:
					if 'five' in word:
						return ['amixer','set','Master','35%']
					else:
						return ['amixer','set','Master','30%']

				if 'fourty' in word:
					if 'five' in word:
						return ['amixer','set','Master','45%']
					else:
						return ['amixer','set','Master','40%']

				if 'fifty' in word:
					if 'five' in word:
						return ['amixer','set','Master','55%']
					else:
						return ['amixer','set','Master','50%']

				if 'sixty' in word:
					if 'five' in word:
						return ['amixer','set','Master','65%']
					else:
						return ['amixer','set','Master','60%']

				if 'seventy' in word:
					if 'five' in word:
						return ['amixer','set','Master','75%']
					else:
						return ['amixer','set','Master','70%']

				if 'eighty' in word:
					if 'five' in word:
						return ['amixer','set','Master','85%']
					else:
						return ['amixer','set','Master','80%']

				if 'ninety' in word:
					if 'five' in word:
						return ['amixer','set','Master','95%']
					else:
						return ['amixer','set','Master','90%']

				if 'hundred' in word:
					return ['amixer','set','Master','100%']


#Music Player Options					
#NEXT
			if 'next' in word:
				if word[0] == 'lux' or word[0] == 'lacer': # rythmbox
					if self.RunningMusic('rhythmbox'):
						return ['rhythmbox-client',' --nopresent',' --next']
				if word[0] == 'alexia' or word[0] == 'pi':
					return ['mpc','next']
			

			if 'prev' in word:
				if word[0] == 'lux' or word[0] == 'lacer': # rythmbox
					if self.RunningMusic("rhythmbox"):
						return ['rhythmbox-client',' --nopresent',' --previous']
				if word[0] == 'alexia' or word[0] == 'pi':
					return ['mpc','prev']

			if 'pause' in  word:
				if word[0] == 'lux' or word[0] == 'lacer': # rythmbox
					if self.RunningMusic("rhythmbox"):
						return ['rhythmbox-client',' --nopresent',' --play-pause']
				if word[0] == 'alexia' or word[0] == 'pi':
					return ['mpc','toggle']

			if 'stop' in word:
				if word[0] == 'lux' or word[0] == 'lacer': # rythmbox
					if self.RunningMusic("rhythmbox"):
						return ['rhythmbox-client',' --nopresent',' --pause']
				if word[0] == 'alexia' or word[0] == 'pi':
					return ['mpc','stop']


			if 'shut' in word:
				if 'down' in word:
					if  'cancel' in word:
						shutdownWarning="Cancel Shutdown"
						try:
							p= subprocess.Popen(['festival','--tts'],stdin=subprocess.PIPE)
							p.communicate(input=shutdownWarning)
							globalPopenList.append(p)
						except OSError:
							print(shutdownWarning)
						return ['sudo','shutdown','-c']

					shutdownWarning="Warning system is going down for halt."
					try:
						p= subprocess.Popen(['festival','--tts'],stdin=subprocess.PIPE)
						p.communicate(input=shutdownWarning)
						globalPopenList.append(p)
					except OSError:
						print(shutdownWarning)
					return ['sudo','shutdown','-h','1']

		else:
			festivalIn="Wrong I. D. please use one of.\n"
			for each in self.ids:
				festivalIn+=" "+each+".\n"
			try:
				p= subprocess.Popen(['festival','--tts'],stdin=subprocess.PIPE)
				p.communicate(input=festivalIn)
				globalPopenList.append(p)
			except OSError:
				print(festivalIn)

		print(word)


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
				self.parse(line.strip('\n')[len(startstring):-len(endstring)])
	
	def parse(self, line):
		# Parse the input
		params = [param.lower() for param in line.split() if param]
		if not '-q' in sys.argv and not '--quiet' in sys.argv:
			print 'Recognized input:', ' '.join(params).capitalize()
		
		# Execute the command, if recognized/supported
		command = self.cmd.parse(params)
		if command:
			try:
				print command
				globalPopenList.append(subprocess.Popen(command,stdout=open("/dev/null"),stderr=open("/dev/null")))
			except OSError:
				festivalIn = "The following command cannot be executed in your system"
				for each in command:
					festivalIn += " "+each
				try:
					p = subprocess.Popen(['festival','--tts'],stdin=subprocess.PIPE)
					p.communicate(festivalIn)
					globalPopenList.append(p)
				except OSError:
					print(festivalIn)
			

if __name__ == '__main__':
	try:
		CommandAndControl(sys.stdin)
	except KeyboardInterrupt:
		for each in globalPopenList:
			each.kill()
			each.wait()
		sys.exit(1)
		
