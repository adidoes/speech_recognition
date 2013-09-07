speech_recognition
==================

Speech recognition: Using julius and voxforge

Usage
=====

Currently the syntax requires you to identify your computer as Lux 
(spoken as: looks), Lacer (spoken as: laser), Alexia, Pi, or Schatz.

After the identification follows a command. The following commands are 
possible:

Volume Control
--------------
Volume control uses amixer to set the Master volume.
volume up/down
volume 1,2,3,4,5,10,15,...,100

mute executes the commands amixer set Master toggle. Synonyms are:
unmute
shut up
silence

Music Player Commands
---------------------
The command.py script separates whether Alexia,Pi, or Lux,Lacer is used 
for identification. For Alexia and Pi, the commands correspond to the 
respective mpc commands. For Lux and Lacer, rhythmbox is used.

next
previous
pause, unpause (spoken as: unpaw)
stop

shutdown
--------

The following commands can be used to turn off, or prevent the 
previously commanded shutdown. Shutdown occurs in one minute.

shut down (two separate words)
cancel shut down (cancel with American pronunciation)

In order to allow for shutdown without password entry add the following 
line to your /etc/sudoers file. Replace user_name appropriately.

%user_name ALL=(ALL) NOPASSWD: /sbin/poweroff /sbin/reboot /sbin/shutdown

