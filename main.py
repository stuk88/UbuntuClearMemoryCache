#!/usr/bin/python
import os
from shlex import split
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

root_pass = ""
command = ""

def runAsRoot(command):
  proc = os.popen(command)

class Handler:
    def onClearPageCache(self, *args):
        runAsRoot("gksudo sysctl vm.drop_caches=1")

    def onClearDentriesAndInodes(self, button):
        runAsRoot("gksudo sysctl vm.drop_caches=2")

    def onClearAll(self, button):
        runAsRoot("gksudo sysctl vm.drop_caches=3")

builder = Gtk.Builder()
builder.add_from_file("main.glade")

builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
