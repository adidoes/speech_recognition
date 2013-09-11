speech_recognition
==================

Speech recognition: Using julius and voxforge

Usage of the basic and shutdown program
=======================================

First the grammar and vocabulary need compilation. To compile the 
mkdfa.pl script should be used. Note: On Ubuntu it is called mkdfa 
in stead of mkdfa.pl.
```
mkdfa.pl basics_and_shutdown
```

Run julius with the control script as
```
julius -C basics_and_shutdown.jconf | ./basics_and_shutdown.py
```

As you can see the control script is written in python v2.

Currently the syntax requires you to identify your computer as Lux 
(spoken as: looks), Lacer (spoken as: lazer), Alexia, or Pi.

After the identification follows a command. The following commands are 
possible:

Volume Control
--------------
Volume control uses amixer to set the Master volume.
* volume up/down
* volume 1,2,3,4,5,10,15,...,100

mute executes the commands amixer set Master toggle. Synonyms are:
* mute
* unmute
* shut up
* silence

Music Player Commands
---------------------
The command script separates whether Alexia,Pi, or Lux,Lacer is used 
for identification. For Alexia and Pi, the commands correspond to the 
respective mpc commands. For Lux and Lacer, rhythmbox is used.

* next
* previous
* pause, unpause (spoken as: unpaw)
* stop

shutdown
--------

The following commands can be used to turn off, or prevent the 
previously commanded shutdown. Shutdown occurs in one minute.


* shut down (two separate words)
* cancel shut down (cancel with American pronunciation)

In order to allow for shutdown without password entry add the following 
line to your /etc/sudoers file. Replace user_name appropriately.

```
%user_name ALL=(ALL) NOPASSWD: /sbin/poweroff /sbin/reboot /sbin/shutdown
```
ISSUES
======

Currently we are unable to prevent julius from outputing the most likely 
command if no good match is found. Due to this reason the ID tag 
contains a number of ERROR outputs. This works for the moment.

The second big issue we encountered is due to to ambient noise level. 
Julius does not differentiate between sound output coming from the 
computer and external sounds. Using headphones there is no issue however 
with satellites louder volume can obstruct the required <sil> tag at the 
beginning and end each identification.
