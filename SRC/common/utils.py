# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import lock
from ooflib.common import debug

import os
import string
import subprocess
import sys
import types
from functools import reduce

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Function to return adjacent pairs of a list, i.e. given [1,2,3],
# it returns [(1,2), (2,3)].
# def list_pairs(lst): # Old version, without generators
#     return [ (lst[i], lst[i+1]) for i in range(len(lst)-1) ]
def list_pairs(lst):
    for i in range(len(lst)-1):
        yield (lst[i],lst[i+1])

# Given a list, return all n*(n-1) pairs of objects in it. 
def unique_pairs(lst):
    for (i, a) in enumerate(lst):
        for (j, b) in enumerate(lst):
            if j < i:
                yield (b,a)
            else:
                break

def pairs(lst):
    for a in lst:
        for b in lst:
            if a is not b:
                yield (a,b)

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#
    
# Function to return 1 if the argument is indexable and 0 otherwise
# def isIndexable(x):
#     try:
#         len(x) # I suppose one could imagine python optimizing this away!
#         return 1
#     except TypeError:
#         return 0
#     except AttributeError:
#         return 0

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#
    
## Commented out because it's not used at the moment.  This can be
## done better by using sets and/or itertools.

# # Used by boundary-condition consistency check to see if small tuples
# # overlap.  Returns a possibly-empty tuple of the intersecting
# # components.
# def tupleIntersect(x,y):
#     result = ()  # Empty tuple.
#     for xvalue in x:
#         for yvalue in y:
#             if xvalue == yvalue:
#                 result+=(xvalue,)
#     return result

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Function to take a list of lists and flatten it into a single list.
def flatten(lols):
    result = []
    for l in lols:
        result += l
    return result

# Unfortunately, this version is much slower:
##   def flatten(lols): return [x for y in lols for x in y]
# and this is even slower than that:
##   def flatten(lols): return reduce(operator.concat, lols, [])

def flatten_all(lols):
    result = []
    for l in lols:
        if isinstance(l, list) or isinstance(l, tuple):
            result += flatten_all(l)
        else:
            result.append(l)
    return result

# Given a template which is a list of lists of lists to arbitrary
# depth, convert the flat datalist to a nested list with the same
# structure.  Each sublist of the result will have the same length as
# the corresponding sublist in the template.
def unflatten(template, datalist):
    which = 0
    result, which = _do_unflatten(template, datalist, which)
    return result

def _do_unflatten(template, datalist, which):
    result = []
    for obj in template:
        if isinstance(obj, list) or isinstance(obj, tuple):
            sublist, which = _do_unflatten(obj, datalist, which)
            result.append(sublist)
        else:
            result.append(datalist[which])
            which += 1
    return result, which

## flatten1 takes a list of lists and returns a list of the contents
## of all the sublist.  It *doesn't* do any recursion on the sublists.
## Creating a list of lists and calling flatten1 on it is much more
## efficient than creating the list by calling 'list += sublist' in a
## loop.

def flatten1(lols):
    length = reduce(lambda x,y: x+len(y), lols, 0)
    flatlist = [None]*length
    offset = 0
    for lst in lols:
        flatlist[offset:offset+len(lst)] = lst
        offset += len(lst)
    return flatlist


#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Given a generator, turn it into a list. Anything else is simply
# returned.

def degenerate(liszt):
    if isinstance(liszt, types.GeneratorType):
        return list(liszt)
    return liszt

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Get a list of the classes to which an object or class belongs.
## TODO: Don't do this. Use inspect.getmro().

def classes(c):
    if isinstance(c, type):
        if not c.__bases__ or c.__bases__ == (object,):
            return [c]
        return [c] +  flatten(map(classes, c.__bases__))
    return classes(c.__class__)

# Get the *names* of the classes to which an object or class belongs.
# This loses namespace information, so it's not as robust as using
# classes().  But it's more readable.
def classnames(c):
    return [cl.__name__ for cl in classes(c)]

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Using PrintableClass as a metaclass allows a class (not the
# instances of the class!) to be printed cleanly. Instead of 
# class A:
#   pass
# print(A)
# ---->  <class '__main__.module.classname'> 
# use
# class A(metaclass=PrintableClass):
#   pass
# print(A)
# ---->  A

class PrintableClass(type):
    def __str__(cls):
        return cls.__name__
    def __repr__(cls):
        return cls.__name__

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Evaluate expressions, statements and files in the main oof namespace.

mainmodule = sys.modules['__main__']

def OOFglobals():
    return mainmodule.__dict__

def OOFexec(command):
    exec(command, mainmodule.__dict__)

def OOFexeclines(commands):
    for command in commands:
        debug.fmsg(command)
        exec(command, mainmodule.__dict__)

def OOFeval(expr):
    return eval(expr, mainmodule.__dict__)

def OOFexecfile(file):
    exec(compile(open(file, "rb").read(), file, 'exec'), mainmodule.__dict__)

# Run a function as if it were defined in the main namespace.
def OOFrun(func, *args, **kwargs):
    # Change the function's globals dict so that it includes stuff
    # from main namespace.  The function's original dict is loaded
    # *after* the main namespace, so that it can override main space
    # definitions if necessary.
    fg = func.__globals__.copy()
    func.__globals__.clear()
    func.__globals__.update(mainmodule.__dict__)
    func.__globals__.update(fg)
    
    func(*args, **kwargs)

    # Restore the original globals dict, so that future calls aren't
    # messed up.
    func.__globals__.clear()
    func.__globals__.update(fg)

# Define an existing object in the main oof namespace.
def OOFdefine(name, obj):
    mainmodule.__dict__[name] = obj

# Safe, restricted evaluation: can't import or do anything malicious.
# Can only be used to evaluate things defined in the main namespace.
# Is used when loading data files.

def OOFeval_r(expr):
    if expr == 'None':
        return None
    return mainmodule.__dict__[expr]

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

### Parse an argument list, e.g. from inside an "eval" when the
### arguments arrive in string form.  IS THIS USED?

    
##def argback(*args,**kwargs):
##    return {"tuple":args, "dictionary":kwargs}

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Construct a name, based on the given name arg, that does not occur
# in the given list of other names.  If the given name isn't in the
# list, return it.  If it is, append "<number>" to it, where 'number'
# is chosen so that the result is unique.

# If the given name is an AutomaticName instance, then an
# AutomaticName instance is returned.

# The list of names passed to uniqueName is almost always a global
# list, and so in a threaded environment we need to prevent
# simultaneous uniqueName calls with the same name list.  Since the
# calls are quick and not done in time sensitive situations, we put a
# single mutex lock inside uniqueName, instead of requiring all
# callers to implement their own lock.

import re

_uniqueNameLock = lock.SLock()

def uniqueName(name, othernames, exclude=None):
    _uniqueNameLock.acquire()
    others = list(othernames)   # othernames might be an iterator
    try:
        if exclude is not None:
            try:
                others.remove(exclude)
            except ValueError:
                pass
        if name not in others:
            return name
        from ooflib.common.IO import automatic # delayed to avoid import loop
        auto = isinstance(name, automatic.AutomaticName)
        # Strip '<number>' suffix, if any.
        basename = re.split('<[0-9]+>$', name)[0]
        # Find any existing names of the form 'basename<number>'.
        expr = re.compile("^" + re.escape(basename) + "<[0-9]+>$")
        matches = list(filter(expr.match, others))
        if matches:
            # Find largest existing "<number>".
            suffixes = [x[len(basename)+1:-1] for x in matches]
            lastsuffix = max(map(eval, suffixes))
        else:
            lastsuffix = 1
        newname = "%s<%d>" % (basename, lastsuffix+1)
        if auto:
            return automatic.AutomaticName(newname)
        return newname
    finally:
        _uniqueNameLock.release()
        
# Special version that uses underscores, for menu names.
def menUniqueName(name, othernames):
    _uniqueNameLock.acquire()
    try:
        if name not in othernames:
            return name
        from ooflib.common.IO import automatic # delayed to avoid import loop
        auto = isinstance(name, automatic.AutomaticName)
        # Strip '_number' suffix, if any.
        basename = re.split('_[0-9]+$', name)[0]
        # Find any existing names of the form 'basename_number'.
        expr = re.compile("^" + re.escape(basename) + "_[0-9]+$")
        matches = list(filter(expr.match, othernames))
        if matches:
            # Find largest existing "number".
            suffixes = [x[len(basename)+1:] for x in matches]
            lastsuffix = max(map(eval, suffixes))
        else:
            lastsuffix = 1
        return "%s_%d" % (basename, lastsuffix+1)
    finally:
        _uniqueNameLock.release()

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Convert a menu item name to the form displayed by the GUI.
# Underscores are replaced by spaces, and double underscores are
# replaced by underscores.  The sleazy implementation here also
# converts double spaces to underscores, but nobody in his right mind
# would put double spaces in menu item names, right?

def underscore2space(name):
    return name.replace("_", " ").replace("  ", "_")

# And the not-quite-inverse.
def space2underscore(name):
    return name.replace(" ", "_")

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

def screenwidth():
    try:
        import curses
        scr = curses.initscr()
        width = scr.getmaxyx()[1]
        curses.endwin()
    except ImportError:
        width = 80
    return width

# Function to format a long string so that it fits into strings of
# length width.  Returns a list of strings guaranteed to be shorter
# than width, provided there are some spaces in there somewhere.
def format(line, width):
    linelist = [stringstrip(ell) for ell in line.split("\n")]
    outlist = []
    for str in linelist:
        while len(str) > width:
            breakpoint = stringrfind(str," ",0,width)
            outlist.append(str[0:breakpoint])
            str = str[breakpoint+1:]
        else:
            outlist.append(str)
    return outlist


#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Minimal ordered dictionary class.  If more functionality is
# required, get someone else's code off the web.  This class just
# ensures that the objects are returned in the order in which they
# were added.


# The optional constructor argument is a list (not a dict!) of (key,
# value) pairs, in the order in which they should appear in the OrderedDict.

## TODO PYTHON3: Add real iterator support.  keys(), values(), and
## items() should return iterators.

class OrderedDict(dict):
    def __init__(self, items=None):
        dict.__init__(self)
        self._keys = []
        if items:
            for key, val in items:
                self.__setitem__(key, val)
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        if key not in self._keys:
            self._keys.append(key)
    def __delitem__(self, key):
        dict.__delitem__(self, key)
        self._keys.remove(key)
    def clear(self):
        self._keys = []
        dict.clear(self)
    def keys(self):
        return self._keys
    def values(self):
        return [dict.__getitem__(self, key) for key in self._keys]
    def items(self):
        return [(key, dict.__getitem__(self, key)) for key in self._keys]
    def reorder(self, keylist):
        # Make sure that our keys are in the order given by keylist.
        # keylist must contain all of our keys, but may contain more.

        ## Check for keys in self._keys that aren't in keylist
        unlisted = [key for key in self._keys if key not in keylist]

        self._keys = [key for key in keylist if key in self._keys] + unlisted
    def __eq__(self, other):
        return (isinstance(other, OrderedDict)
                and self._keys == other._keys
                and super(OrderedDict, self).__eq__(other))
    def replace(self, oldkey, newkey, newval):
        i = self._keys.index(oldkey)
        self._keys[i] = newkey
        dict.__delitem__(self, oldkey)
        dict.__setitem__(self, newkey, newval)
        

import itertools

class OrderedSet:
    def __init__(self, iterable=None):
        self.data = OrderedDict()
        if iterable:
            for item in iterable:
                self.data[item] = 1
    def __len__(self):
        return len(self.data)
    def __contains__(self, item):
        return item in self.data
    def __iter__(self):
        return iter(self.data.keys())
    def add(self, item):
        self.data[item] = 1
    def remove(self, item):
        del self.data[item]
    def discard(self, item):
        try:
            del self.data[item]
        except KeyError:
            pass
    def replace(self, old, new):
        self.data.replace(old, new, 1)
    def clear(self):
        self.data = OrderedDict()
    def union(self, other):
        result = OrderedSet(list(self.data.keys()))
        for item in other:
            result.add(item)
        return result
    def __or__(self, other):
        if not isinstance(other, OrderedSet):
            return NotImplemented
        return self.union(other)
    def intersection(self, other):
        common = filter(lambda x: x in other.data, self)
        return self.__class__(common)
    def __and__(self, other):
        if not isinstance(other, OrderedSet):
            return NotImplemented
        return self.intersection(other)
    def copy(self):
        return OrderedSet(self)
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self.data.keys()))
    def __eq__(self, other):
        return self.data == other.data
    def __ne__(self, other):
        return self.data != other.data
    def __add__(self, other):
        return self.union(other)

    __str__ = __repr__
        
        
#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# A list-like object in which space can be reserved so that it doesn't
# have to be reallocated all the time.  It doesn't support all of the
# slice operations that a real list would. (__del__ and __setitem__
# aren't provided for slices.  __getitem__ is.)

## TODO PYTHON3: Make ReservableList iterable.


class ReservableList:
    def __init__(self, n=0):
        self._list = [None]*n
        self._length = 0
    def __len__(self):
        return self._length
    def __getitem__(self, i):
        if isinstance(i, slice):
            start, stop, step = i.indices(self._length)
            # No need to check bounds on slices.
            return self._list[start:stop:step]
        else:                           # not a slice
            if i >= self._length or i < -self._length:
                raise IndexError(i, "is out of range")
            if i >= 0:
                return self._list[i]
            return self._list[self._length+i] # i < 0
    def __setitem__(self, i, val):
        if i >= 0:
            if i >= self._length:
                raise IndexError("Reservable list index out of range")
            self._list[i] = val
        else:
            if i < -self._length:
                raise IndexError("Reservable list index out of range")
            self._list[self._length+i] = val
    def capacity(self):
        return len(self._list)
    def reserve(self, size):
        if size <= len(self._list):
            return
        new_list = self._list + [None]*(size-len(self._list))
        self._list = new_list
    def reverse(self):
        oldsize = len(self._list)
        newlist = self._list[:self._length]
        newlist.reverse()
        self._list = newlist + [None]*(oldsize - self._length)
    def append(self, x):
        if self._length == len(self._list):
            self._list.append(x)
        else:
            self._list[self._length] = x
        self._length += 1
    def __delitem__(self, i):
        oldsize = len(self._list)
        if isinstance(i, int) and i >= self._length or i<-self._length+1:
            raise IndexError(i, "is out of range")
        del self._list[i]
        self._length -= oldsize - len(self._list)
    def __repr__(self):
        return repr(self._list[:self._length])
    def __add__(self, other):
        return self._list[:self._length] + other
    def __radd__(self, other):
        return other + self._list[:self._length]
    def sort(self):
        if self._length == len(self._list):
            self._list.sort()
        else:
            self._list[:self._length] = sorted(self._list[:self._length])

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

import os

# Some functions needed for using patterns to specify multiple files.

# Check if a filename matches a pattern.
def matchpattern(pattern, filename):
    # "*" in regular expressions doesn't have the same effect as
    # "*" in file pattern matching, in re's it is greedy, so we
    # need to replace it with ".*?".  We also need to escape the
    # string.
    escaped_pattern = stringreplace(re.escape(os.path.basename(pattern)),"\\*",".*?")
    match = re.match(escaped_pattern, filename)
    if match is None:
        return False
    span = match.span()
    # is this the right condition?
    if span[0]==0 and span[1] == len(filename):
        return True
    return False

# we need a special function where * means any integer.
def matchvtkpattern(pattern, filename):
    # "*" in regular expressions doesn't have the same effect as
    # "*" in file pattern matching, in re's it is greedy, so we
    # need to replace it with ".*?".  We also need to escape the
    # string.
    escaped_pattern = stringreplace(re.escape(os.path.basename(pattern)),"\\*","[0-9]*")
    match = re.match(escaped_pattern, filename)
    if match is None:
        return False
    span = match.span()
    # is this the right condition?
    if span[0]==0 and span[1] == len(filename):
        return True
    return False

def countmatches(pattern, dirname, matchfunction=matchpattern):
    try:
        items = os.listdir(dirname)
    except:
        return 0
    matchcount = 0
    # TODO 3D: we should probably check that the items are not actually
    # directories
    if pattern == "*":
        return len(items)
    for item in items:
        if matchfunction(pattern, item):
            matchcount += 1
    return matchcount


#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

def _find_machine_epsilon():
    eps = 1.0
    while 1.0 + eps/2. != 1.0:
        eps = eps/2.
    return eps

machine_epsilon = _find_machine_epsilon()

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Built-in all() isn't defined in python < 2.5.
## TODO: Remove this if we stop supporting 2.4.

try:
    all
except NameError:
    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True
    __builtins__['all'] = all

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

# Memory monitoring.  Prints the current memory usage to a file.  Put
# calls to memusage() at points where you want to know how much memory
# is being used.  This only works on Linux at the moment.

memfile = None

def startMemoryMonitor(filename):
    global memfile
    memfile = open(filename, "w")
    memusage("startMemoryMonitor")

def stopMemoryMonitor():
    global memfile
    if memfile is not None:
        memfile.close()
        memfile = None

def get_memusage_str():
    pid = os.getpid()
    if sys.platform == 'darwin':
        vmmap = subprocess.check_output(["vmmap", "-summary", repr(pid)])
        lines = vmmap.split('\n')
        # The trouble here is that the output from vmmap requires some
        # parsing, and I don't know if whatever is done here will be
        # robust.  I am tempted not to bother with it until it's
        # actually needed, if ever.

        # There are two main blocks of output below the header.  One
        # is headed "REGION TYPE" and one is "MALLOC ZONE".  We may
        # just want to look at the second.  REGION TYPE seems to
        # always have a line that begins with "TOTAL" followed by 8
        # numbers in the form xxxG, xxxM, or xxxK.  The first number
        # is the column marked "VIRTUAL SIZE" and may be what we want.
        # Or maybe we only want the same number from the "MALLOC ZONE"
        # block.  But that block doesn't always have a TOTAL line.
        # Sometimes it has only one line, marked
        # "DefaultMallocZone_0x....".  Presumably TOTAL is omitted if
        # there's only one contribution.

    elif sys.platform == 'linux2':
        pmap = subprocess.check_output(["pmap", repr(pid)])
        # pmap contains a long string with embedded newlines. It ends with
        # "\n total XXXXXK\n" where XXXXX is the number we want.
        mem = pmap.rsplit('\n')[-2].split()[1][:-1]
        return mem

def get_memusage():
    m = get_memusage_str()
    return int(m[:-1])          # strip off the K and convert to int
    
def memusage(comment):
    if memfile:
        print(get_memusage_str(), '#', comment, file=memfile)
        memfile.flush()

# Make memusage available in OOF scripts
OOFdefine('memusage', memusage)
OOFdefine('get_memusage', get_memusage)

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

## Hacks to make switching from Python2 easier.

# Functions that used to be in the string module are now just string
# methods.  Defining these functions here lets us simply delete a "."
# whereever the old function was used, [eg change string.join(strings,
# sep) to stringjoin(strings, sep)] which is faster to do and less
# error-prone.

## TODO? Get rid of these functions and call the string methods directly.

def stringjoin(strngs, sep):
    return sep.join(strngs)

def stringfind(source, target, *args, **kwargs):
    return source.find(target, *args, **kwargs)

def stringrfind(source, target, *args, **kwargs):
    return source.rfind(target, *args, **kwargs)

def stringsplit(source, *args, **kwargs):
    return source.split(*args, **kwargs)

def stringreplace(strng, old, new, *args, **kwargs):
    return strng.replace(old, new, *args, **kwargs)

def stringstrip(strng, *args, **kwargs):
    return strng.strip(*args, **kwargs)

def stringlstrip(strng, *args, **kwargs):
    return strng.lstrip(*args, **kwargs)

def stringrstrip(strng, *args, **kwargs):
    return strng.rstrip(*args, **kwargs)

#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#=*=#

if __name__=='__main__':
    l0 = [0, [1,2],[3,[4]], 5]
    l1 = ['zero', 'one', 'two', 'three', 'four', 'five']
    print(unflatten(l0, l1))
