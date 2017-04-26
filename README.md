# OpenSeesAPI
![alt text](https://travis-ci.org/nassermarafi/OpenSeesAPI.svg?branch=master)

OSAPI short for OpenSeesAPI is a python package that is used to write [OpenSees](http://opensees.berkeley.edu) tcl scripts quickly.
OSAPI is written using an object-oriented programing style making easy to interact with other commonly used python packages like numpy, scipy and maptlotlib.


## Installation instructions

- Make sure you have OpenSees [downloaded](http://opensees.berkeley.edu/OpenSees/user/download.php) and installed (including the required tcl libraries).
- Add OpenSees (or OpenSeesSP/OpenSeesMP) to your system path. This can be done easily in the command prompt or terminal.

Windows Users:

<pre><code>set PATH=%PATH%;OpenSeesPath
</code></pre>

Mac/Linux Users:

<pre><code>export PATH=$PATH:~/OpenSeesPath
</code></pre>

- Install OpenSeesAPI using pip. This can be done using the following command.

<pre><code>pip install OpenSeesAPI
</code></pre>

## Advance Users
Advanced users (who intends to add classes or change the source code) can also clone this repository and then setup it in develop mode which allows you to make changes to the original source files as you run OSAPI (this is recommended as I have not included all the OpenSees classes). 

Instructions:
- Add OpenSees to your path
- In your working directory, clone GitHub respository

<pre><code>git clone https://github.com/nassermarafi/OpenSeesAPI
</code></pre>

- Install OSAPI in develop mode

<pre><code>python setup.py develop
</code></pre>

- Start developing OSAPI and make some pull requests

## Example Scripts

Three Example Script using OSAPI are available:
- [SampleScript1.py](https://raw.githubusercontent.com/nassermarafi/OpenSeesAPI/master/test/SampleScript1.py) => SDOF System with a Deteriorating Ibarra Spring
- [SampleScript2.py](https://raw.githubusercontent.com/nassermarafi/OpenSeesAPI/master/test/SampleScript2.py) => 40 Story PEER - Tall Building Initiative Building with Buckling Restrained Braced Frames
- [SampleScript3.py](https://raw.githubusercontent.com/nassermarafi/OpenSeesAPI/master/test/SampleScript3.py) => Moment Curvature analysis for a concrete column
- [SampleScript4.py](https://raw.githubusercontent.com/nassermarafi/OpenSeesAPI/master/test/SampleScript4.py) => Dynamic Analysis of a Steel Moment Frame Structure ([Recreation of Sample OpenSees TCL Script](http://opensees.berkeley.edu/wiki/index.php/Pushover_Analysis_of_2-Story_Moment_Frame))

I am working on more. Email me (marafi [at] uw dot edu) if you have suggestions or need something specific.

## License

The MIT License (MIT)

Copyright (c) 2016 Nasser Marafi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
