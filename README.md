![](http://i.imgur.com/ZnHpuWF.jpg)

freezeray
=========

Freeze a requirements.txt based on what's currently installed

### Installation ###

`pip install freezeray`

### What's It Do? ###

Freezeray takes an existing requirements.txt file you have and writes a new file with the currently installed versions of all the packages in your input file *plus* their dependencies.

It's basically `pip freeze` for a subset of the packages you have installed at any given time.

### Usage ###

The command line tool reads in an input requirements.txt file and writes to a separate output file. Once you've installed, it's as easy as running this:

```
freezeray <path to input file> <path to output file>
```
