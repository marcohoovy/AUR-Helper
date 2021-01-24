#!/bin/bash
#--------------------------------------------------------------------------#
#                               Made by Harvey298                          #
#               Simple AUR Helper made in 6 lines!  23 Jan 2021            #
#                                                                          #
#--------------------------------------------------------------------------#
import os
packagename = input("The package name:")
packageurl = "https://aur.archlinux.org/" + packagename + ".git"
print("Downloading package from the AUR")
os.system("git clone " + packageurl)
os.system("cd " + packagename + " && makepkg -si -j 5")
