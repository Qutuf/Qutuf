# 2007/11/08
# Version 0.2.6
# pathutils.py
# Functions useful for working with files and paths.
# http://www.voidspace.org.uk/python/recipebook.shtml#utils

# Copyright Michael Foord 2004
# Released subject to the BSD License
# Please see http://www.voidspace.org.uk/python/license.shtml

# For information about bugfixes, updates and support, please join the Pythonutils mailing list.
# http://groups.google.com/group/pythonutils/
# Comments, suggestions and bug reports welcome.
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

"""
This module contains convenience functions for working with files and paths.
"""

from __future__ import generators
import os
import sys
import time

__version__ = '0.2.6'

__all__ = (
    'readlines',
    'writelines',
    'readbinary',
    'writebinary',
    'readfile',
    'writefile',
    'tslash',
    'relpath',
    'splitall',
    'walkfiles',
    'walkdirs',
    'walkemptydirs',
    'formatbytes',
    'fullcopy',
    'import_path',
    'onerror',
    'get_main_dir',
    'main_is_frozen',
    'Lock',
    'LockError',
    'LockFile',
    '__version__',
    )

######################################
# Functions to read and write files in text and binary mode.

def readlines(filename):
    """Passed a filename, it reads it, and returns a list of lines. (Read in text mode)"""
    filehandle = open(filename, 'r')
    outfile = filehandle.readlines()
    filehandle.close()
    return outfile

def writelines(filename, infile, newline=False):
    """
    Given a filename and a list of lines it writes the file. (In text mode)
    
    If ``newline`` is ``True`` (default is ``False``) it adds a newline to each
    line.
    """
    filehandle = open(filename, 'w')
    if newline:
        infile = [line + '\n' for line in infile]
    filehandle.writelines(infile)
    filehandle.close()

def readbinary(filename):
    """Given a filename, read a file in binary mode. It returns a single string."""
    filehandle = open(filename, 'rb')
    thisfile = filehandle.read()
    filehandle.close()
    return thisfile

def writebinary(filename, infile):
    """Given a filename and a string, write the file in binary mode. """
    filehandle = open(filename, 'wb')
    filehandle.write(infile)
    filehandle.close()

def readfile(filename):
    """Given a filename, read a file in text mode. It returns a single string."""
    filehandle = open(filename, 'r')
    outfile = filehandle.read()
    filehandle.close()
    return outfile

def writefile(filename, infile):
    """Given a filename and a string, write the file in text mode."""
    filehandle = open(filename, 'w')
    filehandle.write(infile)
    filehandle.close()
    
####################################################################
# Some functions for dealing with paths

def tslash(apath):
    """
    Add a trailing slash (``/``) to a path if it lacks one.
    
    It doesn't use ``os.sep`` because you end up in trouble on windoze, when you
    want separators for URLs.
    """
    if apath and apath != '.' and not apath.endswith('/') and not apath.endswith('\\'):
        return apath + '/'
    else:
        return apath

def relpath(origin, dest):
    """
    Return the relative path between origin and dest.
    
    If it's not possible return dest.
    
    
    If they are identical return ``os.curdir``
    
    Adapted from `path.py <http://www.jorendorff.com/articles/python/path/>`_ by Jason Orendorff. 
    """
    origin = os.path.abspath(origin).replace('\\', '/')
    dest = os.path.abspath(dest).replace('\\', '/')
    #
    orig_list = splitall(os.path.normcase(origin))
    # Don't normcase dest!  We want to preserve the case.
    dest_list = splitall(dest)
    #
    if orig_list[0] != os.path.normcase(dest_list[0]):
        # Can't get here from there.
        return dest
    #
    # Find the location where the two paths start to differ.
    i = 0
    for start_seg, dest_seg in zip(orig_list, dest_list):
        if start_seg != os.path.normcase(dest_seg):
            break
        i += 1
    #
    # Now i is the point where the two paths diverge.
    # Need a certain number of "os.pardir"s to work up
    # from the origin to the point of divergence.
    segments = [os.pardir] * (len(orig_list) - i)
    # Need to add the diverging part of dest_list.
    segments += dest_list[i:]
    if len(segments) == 0:
        # If they happen to be identical, use os.curdir.
        return os.curdir
    else:
        return os.path.join(*segments).replace('\\', '/')

def splitall(loc):
    """
    Return a list of the path components in loc. (Used by relpath_).
    
    The first item in the list will be  either ``os.curdir``, ``os.pardir``, empty,
    or the root directory of loc (for example, ``/`` or ``C:\\).
    
    The other items in the list will be strings.
        
    Adapted from *path.py* by Jason Orendorff.
    """
    parts = []
    while loc != os.curdir and loc != os.pardir:
        prev = loc
        loc, child = os.path.split(prev)
        if loc == prev:
            break
        parts.append(child)
    parts.append(loc)
    parts.reverse()
    return parts

#######################################################################
# a pre 2.3 walkfiles function - adapted from the path module by Jason Orendorff

join = os.path.join
isdir = os.path.isdir
isfile = os.path.isfile

def walkfiles(thisdir):
    """
    walkfiles(D) -> iterator over files in D, recursively. Yields full file paths.
    
    Adapted from path.py by Jason Orendorff.
    """
    for child in os.listdir(thisdir):
        thischild = join(thisdir, child)
        if isfile(thischild):
            yield thischild
        elif isdir(thischild):
            for f in walkfiles(thischild):
                yield f
                
def walkdirs(thisdir):
    """
    Walk through all the subdirectories in a tree. Recursively yields directory
    names (full paths).
    """
    for child in os.listdir(thisdir):
        thischild = join(thisdir, child)
        if isfile(thischild):
            continue
        elif isdir(thischild):
            for f in walkdirs(thischild):
                yield f
            yield thischild

def walkemptydirs(thisdir):
    """
    Recursively yield names of *empty* directories.
    
    These are the only paths omitted when using ``walkfiles``.
    """
    if not os.listdir(thisdir):
        # if the directory is empty.. then yield it
        yield thisdir   
    for child in os.listdir(thisdir):
        thischild = join(thisdir, child)
        if isdir(thischild):
            for emptydir in walkemptydirs(thischild):
                yield emptydir

###############################################################
# formatbytes takes a filesize (as returned by os.getsize() )
# and formats it for display in one of two ways !!

def formatbytes(sizeint, configdict=None, **configs):
    """
    Given a file size as an integer, return a nicely formatted string that
    represents the size. Has various options to control it's output.
    
    You can pass in a dictionary of arguments or keyword arguments. Keyword
    arguments override the dictionary and there are sensible defaults for options
    you don't set.
    
    Options and defaults are as follows :
    
    *    ``forcekb = False`` -         If set this forces the output to be in terms
    of kilobytes and bytes only.
    
    *    ``largestonly = True`` -    If set, instead of outputting 
        ``1 Mbytes, 307 Kbytes, 478 bytes`` it outputs using only the largest 
        denominator - e.g. ``1.3 Mbytes`` or ``17.2 Kbytes``
    
    *    ``kiloname = 'Kbytes'`` -    The string to use for kilobytes
    
    *    ``meganame = 'Mbytes'`` - The string to use for Megabytes
    
    *    ``bytename = 'bytes'`` -     The string to use for bytes
    
    *    ``nospace = True`` -        If set it outputs ``1Mbytes, 307Kbytes``, 
        notice there is no space.
    
    Example outputs : ::
    
        19Mbytes, 75Kbytes, 255bytes
        2Kbytes, 0bytes
        23.8Mbytes
    
    .. note::
    
        It currently uses the plural form even for singular.
    """
    defaultconfigs = {  'forcekb' : False,
                        'largestonly' : True,
                        'kiloname' : 'Kbytes',
                        'meganame' : 'Mbytes',
                        'bytename' : 'bytes',
                        'nospace' : True}
    if configdict is None:
        configdict = {}
    for entry in configs:
        # keyword parameters override the dictionary passed in
        configdict[entry] = configs[entry]
    #
    for keyword in defaultconfigs:
        if not configdict.has_key(keyword):
            configdict[keyword] = defaultconfigs[keyword]
    #
    if configdict['nospace']:
        space = ''
    else:
        space = ' '
    #
    mb, kb, rb = bytedivider(sizeint)
    if configdict['largestonly']:
        if mb and not configdict['forcekb']:
            return stringround(mb, kb)+ space + configdict['meganame']
        elif kb or configdict['forcekb']:
            if mb and configdict['forcekb']:
                kb += 1024*mb
            return stringround(kb, rb) + space+ configdict['kiloname']
        else:
            return str(rb) + space + configdict['bytename']
    else:
        outstr = ''
        if mb and not configdict['forcekb']:
            outstr = str(mb) + space + configdict['meganame'] +', '
        if kb or configdict['forcekb'] or mb:
            if configdict['forcekb']:
                kb += 1024*mb
            outstr += str(kb) + space + configdict['kiloname'] +', '
        return outstr + str(rb) + space + configdict['bytename']

def stringround(main, rest):
    """
    Given a file size in either (mb, kb) or (kb, bytes) - round it
    appropriately.
    """
    # divide an int by a float... get a float
    value = main + rest/1024.0
    return str(round(value, 1))

def bytedivider(nbytes):
    """
    Given an integer (probably a long integer returned by os.getsize() )
    it returns a tuple of (megabytes, kilobytes, bytes).
    
    This can be more easily converted into a formatted string to display the
    size of the file.
    """
    mb, remainder = divmod(nbytes, 1048576)
    kb, rb = divmod(remainder, 1024)
    return (mb, kb, rb)

########################################

def fullcopy(src, dst):
    """
    Copy file from src to dst.
    
    If the dst directory doesn't exist, we will attempt to create it using makedirs.
    """
    import shutil
    if not os.path.isdir(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    shutil.copy(src, dst)    

#######################################

def import_path(fullpath, strict=True):
    """
    Import a file from the full path. Allows you to import from anywhere,
    something ``__import__`` does not do.
    
    If strict is ``True`` (the default), raise an ``ImportError`` if the module
    is found in the "wrong" directory.
    
    Taken from firedrop2_ by `Hans Nowak`_
    
    .. _firedrop2: http://www.voidspace.org.uk/python/firedrop2/
    .. _Hans Nowak: http://zephyrfalcon.org
    """
    path, filename = os.path.split(fullpath)
    filename, ext = os.path.splitext(filename)
    sys.path.insert(0, path)
    try:
        module = __import__(filename)
    except ImportError:
        del sys.path[0]
        raise
    del sys.path[0]
    #
    if strict:
        path = os.path.split(module.__file__)[0]
        # FIXME: doesn't *startswith* allow room for errors ?
        if not fullpath.startswith(path):
            raise ImportError("Module '%s' found, but not in '%s'" ,\
                  filename, fullpath)
#            raise ImportError, "Module '%s' found, but not in '%s'" % (
#                  filename, fullpath)
    #
    return module

##############################################################################
# These functions get us our directory name
# Even if py2exe or another freeze tool has been used

def main_is_frozen():
    """Return ``True`` if we're running from a frozen program."""
    import imp
    return (
        # new py2exe
        hasattr(sys, "frozen") or
        # tools/freeze
        imp.is_frozen("__main__"))

def get_main_dir():
    """Return the script directory - whether we're frozen or not."""
    if main_is_frozen():
        return os.path.abspath(os.path.dirname(sys.executable))
    return os.path.abspath(os.path.dirname(sys.argv[0]))

##############################

def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.
    
    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

##########################################################
# A set of object for providing simple, cross-platform file locking

class LockError(IOError):
    """
    The generic error for locking - it is a subclass of ``IOError``.
    # PyUML: Do not remove this line! # XMI_ID:_hTbvYo34Ed-gg8GOK1TmhA
    """

class Lock(object):
    """
    A simple file lock, compatible with windows and Unixes.
    # PyUML: Do not remove this line! # XMI_ID:_hTbvY434Ed-gg8GOK1TmhA
    """

    def __init__(self, filename, timeout=5, step=0.1):
        """
        Create a ``Lock`` object on file ``filename``
        
        ``timeout`` is the time in seconds to wait before timing out, when
        attempting to acquire the lock.
        
        ``step`` is the number of seconds to wait in between each attempt to
        acquire the lock.
        
        """
        self.timeout = timeout
        self.step = step
        self.filename = filename
        self.locked = False

    def lock(self, force=True):
        """
        Lock the file for access by creating a directory of the same name (plus
        a trailing underscore).
        
        The file is only locked if you use this class to acquire the lock
        before accessing.
        
        If ``force`` is ``True`` (the default), then on timeout we forcibly
        acquire the lock.
        
        If ``force`` is ``False``, then on timeout a ``LockError`` is raised.
        """
        if self.locked:
            raise LockError('%s is already locked' % self.filename)
        t = 0
        name = self._mungedname()
        while t < self.timeout:
            t += self.step
            try:
                if os.path.isdir(name):
                    raise os.error
                else:
                    os.mkdir(name)
            except err:
                time.sleep(self.step)
            else:
                self.locked = True
                return
        if force:
            self.locked = True
        else:
            raise LockError('Failed to acquire lock on %s' % self.filename)

    def unlock(self, ignore=True):
        """
        Release the lock.
        
        If ``ignore`` is ``True`` and removing the lock directory fails, then
        the error is surpressed. (This may happen if the lock was acquired
        via a timeout.)
        """
        if not self.locked:
            raise LockError('%s is not locked' % self.filename)
        self.locked = False
        try:
            os.rmdir(self._mungedname())
        except  err:
            if not ignore:
                raise LockError('unlocking appeared to fail - %s' %
                    self.filename)

    def _mungedname(self):
        """
        Override this in a subclass if you want to change the way ``Lock`` 
        creates the directory name.
        """
        return self.filename + '_'

    def __del__(self):
        """Auto unlock when object is deleted."""
        if self.locked:
            self.unlock()

class LockFile:
    """
    A file like object with an exclusive lock, whilst it is open.
    
    The lock is provided by the ``Lock`` class, which creates a directory
    with the same name as the file (plus a trailing underscore), to indicate
    that the file is locked.
    
    This is simple and cross platform, with some limitations :
    
        * Unusual process termination could result in the directory
          being left.
        * The process acquiring the lock must have permission to create a
          directory in the same location as the file.
        * It only locks the file against other processes that attempt to
          acquire a lock using ``LockFile`` or ``Lock``.
    # PyUML: Do not remove this line! # XMI_ID:_hT4bcI34Ed-gg8GOK1TmhA
    """

    def __init__(self, filename, mode='r', bufsize=-1, timeout=5, step=0.1,
        force=True):
        """
        Create a file like object that is locked (using the ``Lock`` class)
        until it is closed.
        
        The file is only locked against another process that attempts to
        acquire a lock using ``Lock`` (or ``LockFile``).
        
        The lock is released automatically when the file is closed.
        
        The filename, mode and bufsize arguments have the same meaning as for
        the built in function ``open``.
        
        The timeout and step arguments have the same meaning as for a ``Lock``
        object.
        
        The force argument has the same meaning as for the ``Lock.lock`` method.
        
        A ``LockFile`` object has all the normal ``file`` methods and
        attributes.
        """
        Lock.__init__(self, filename, timeout, step)
        # may raise an error if lock is ``False``
        self.lock(force)
        # may also raise an error
        self._file = open(filename, mode, bufsize)

    def close(self, ignore=True):
        """
        close the file and release the lock.
        
        ignore has the same meaning as for ``Lock.unlock``
        """
        self._file.close()
        self.unlock(ignore)

    def __getattr__(self, name):
        """delegate appropriate method/attribute calls to the file."""
        return getattr(self._file, name)

    def __setattr__(self, name, value):
        """Only allow attribute setting that don't clash with the file."""
        if not '_file' in self.__dict__:
            Lock.__setattr__(self, name, value)
        elif hasattr(self._file, name):
            return setattr(self._file, name, value)
        else:
            Lock.__setattr__(self, name, value)

    def __del__(self):
        """Auto unlock (and close file) when object is deleted."""
        if self.locked:
            self.unlock()
            self._file.close()

