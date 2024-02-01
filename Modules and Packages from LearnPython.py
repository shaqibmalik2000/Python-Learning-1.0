# Modules and Packages

# game.py implements the game
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means if script executes, then
# main() will execute
if _name_ == '_main_':
    main()

# Draw module

def draw_game():
    ...

def clear_screen(screen):
    ...

# game mod imports the draw mod, which allows it to use functions within the other module.
# main function uses local function play_game to run the game, then draws the result with draw_game.
# dot operator specifies which mod the function is in
# to reference draw_game function from game mod, we import draw mod and call draw.draw_game()
    
# when import draw directive runs, the python interpreter looks for file in directory where script executes with mod name and .py suffix.
# looks for draw.py. If found, it imports. If not found, it continues to look for mods.
    
# when importing a mod, a .pyc file is created and this is called a compiled python file.
# Python compiles files into bytecode so that it won't have to parse files each time mods are loaded.
# if .pyc file exists, it gets loaded over the .py file.

# Import module objects to current namespace
# game.py - import the draw mod
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)
# mod name does not come before draw_game, since this is specifically mod name using the import command.
# advantage of this is there is not a need to reference mod over and over. However, namespace cannot have two objects with same name.
# So import command may replace an existing object in the namespace.

# Import all objects from a mod using import * command
# game.py import from draw mod
from draw import *

def main():
    result = play_game()
    draw_game(result)
# Risky as changes in mod may affect the mod that imports it. Though shorter, and doesn't require you to specify every object you want to import from the mod.
    
# Custom name import
# Mods may have any name. Good when importing mod conditionally to use the same name in the rest of the code.
    
# Example of having two draw mods with slightly different names:
# game.py imports the draw mod
if visual_mode:
    # in visual mode, we draw using graphics.
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def_main():
    result = play_game()
    # this can be either visual or textual depending on visual_mode
    draw.draw_game(result)

# Module initialization
# First time a mode is loaded into a running script, it is initialized by executing the code in the mod once.
# If another mod in the code imports the same mod twice, it will not load again, so local variables inside the mod act as a "singleton," meaning they are initialized once.

# draw.py
def draw_game():
    # when clearing the screen we can use the main screen object initialized in this mod
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()

# Extend module load path
# Few ways to tell interpreter where to look for mods, aside from the default local directory and built-in mods.
# Environment variable called PYTHONPATH to specify additional directories to look for mods like so:
PYTHONPATH=/foo python game.py 
#this runs game.py, and makes the script load mods from the foo directory, and the local directory.

# May also use sys.path.append function. Execute it before running the import command.
sys.path.append("/foo")
# Now the foo directory has been added to the list of paths where mods are looked for.

# Explore built-in modules
# THere is a full list of built-in ods in the Python standard library
# Two important functions come in handy when exploring mods in Python - the dir and help functions.
# To import the mod urllib, which helps us create read data from URLs, we import the mod
# import library
import urllib
# use it
urllib.urlopen(...)

# Search for functions that are implemented in each module by using the dir function

>>> import urllib
>>> dir(irllib)
# ['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', 
# '__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies', 
# '_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', 
# '_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', 
# '_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 
# 'addinfo', 'addinfourl', 'always_safe', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 
# 'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'main', 'noheaders', 'os', 
# 'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 
# 'quote_plus', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 
# 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test', 'test1', 
# 'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 
# 'urlopen', 'urlretrieve']

# When the function is found in the module, we can read about it with the help function using the interpreter:
help(urlib.urlopen)

# Writing packages
# Contains multiple packages and modules. Just like directories, but with requirements.
# Each package must contain a special fil called _init_.py. This file can be empty, but tells the directory that it is in a Python package. Imports the same way as a module.
# Creating a directory called foo (package name). THen make a mod inside the package called bar.
# Then the _init_.py file is added into the foo directory.
# To use mod bar, there are two ways to import. First way:
import foo.bar
# Second way:
from foo import bar

# _init_.py file can decide which mod the package exports as the API, while keeping other mods internal, by overriding the _all_ variable like so:
_init_.py:
_all_ = ["bar"]

# Exercise
# Print an alphabetically sorted list of all functions in re module containing the word find:

import re

# My code here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))