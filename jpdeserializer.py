"""
JP Deserializer - Java-Python Deserializer

Created by: Daniele Linguaglossa
Mail: danielelinguaglossa@gmail.com
Date: 28/06/2017

JP Deserializer is an interactive console which allow to inspect Java serialized objects, you can view, modify and save
any serialized object. It's even possible to create Object from scratch and save them!
"""

from java.io import ObjectInputStream, FileInputStream, FileOutputStream, BufferedOutputStream, ObjectOutputStream
from java.lang import ClassNotFoundException
import argparse
import jarray
import array
import types
import json
import code
import java
import org
import sys
import os

class classPathHacker(object):
    import java.lang.reflect.Method
    import java.io.File
    import java.net.URL
    import java.net.URLClassLoader

    def addFile(self, s):
        f = self.java.io.File(s)
        u = f.toURL()
        a = self.addURL(u)
        return a

    def addURL(self, u):
        sysloader = self.java.lang.ClassLoader.getSystemClassLoader()
        sysclass = self.java.net.URLClassLoader
        method = sysclass.getDeclaredMethod("addURL", [self.java.net.URL])
        a = method.setAccessible(1)
        jar_a = jarray.array([u], self.java.lang.Object)
        b = method.invoke(sysloader, [u])
        return u


parser = argparse.ArgumentParser()
parser.add_argument("-obj", metavar="object", dest="object", help="Serialized Object", required=True)
parser.add_argument("-cp", dest="classpath", default=[], metavar="classpath", help="List of jar to include in classpath", nargs="*")
args = parser.parse_args()

jarLoad = classPathHacker()
for element in args.classpath:
    try:
            a = jarLoad.addFile(os.path.abspath(element))
    except:
            sys.exit (sys.exc_info())
inputFileStream = FileInputStream(args.object)
objectInputStream = ObjectInputStream(inputFileStream)

try:
    deserialized = objectInputStream.readObject()
except ClassNotFoundException as cnf:
    print("Error: Unable to decode object, missing class '{0}'".format(cnf.message))
    sys.exit(0)

def import_all(package):
    """
    Import all classes in a package
    """
    for element in dir(package):
        tmp = getattr(package,str(element))
        if type(tmp).__name__ == "Class":
            clazz = getattr(package, element)
            globals().update({element: clazz})
        elif type(tmp).__name__ == "javapackage":
            import_all(tmp)

def custom_to_list(obj):
    for i in range(0, len(obj)):
        if type(obj[i]) == array.array:
            obj[i] == obj[i].tolist()
            obj[i] = custom_to_list(obj[i])
    if type(obj) == array.array:
        return obj.tolist()
    else:
        return obj

class JavaObject(object):
    """
    Represent our Java deserialized object
    """
    def __init__(self, obj):
        self.obj = obj
        sys.displayhook = self.show_graph

    def __getitem__(self, item):
        return self.obj.__getitem__(item)

    def show_graph(self, obj, last_len=0, called=0, prefix=""):

        if type(obj) == JavaObject:
            obj = obj.obj

        def is_iterable(obj):
            if type(obj) == list:
                return True
            else:
                return False

        def len_2_graph(length, times):
            tmp = ""
            try:
                how = length / times
            except:
                return ""
            for _ in range(0, times):
                if _ == times-1:
                    tmp += u"{0}\u2520".format(" " * how)
                else:
                    tmp += u"{0}\u2503".format(" " * how)

            return tmp

        if is_iterable(obj):
            print(u"{0}  {1}<{2}>".format(len_2_graph(last_len, called), "[{0}]".format(prefix) if prefix else "", type(obj).__name__))
            last_len += len(type(obj).__name__) + 3
            for index in range(0, len(obj)):
                self.show_graph(obj[index], last_len, called=called+1, prefix=str(index))
        else:
            if type(obj) in [unicode]:
                print u"{0}  {1}(String) => {2}".format(len_2_graph(last_len, called), "[{0}]".format(prefix) if prefix else "", obj)
            else:
                print u"{0}  {1}({2}) => {3}".format(len_2_graph(last_len, called), "[{0}]".format(prefix) if prefix else "", type(obj).__name__, obj)

def serialize(obj, filename):
    """
    Serialize an object
    """
    if type(obj) == JavaObject:
        obj = obj.obj
    try:
        outfile = FileOutputStream(filename)
        output = ObjectOutputStream(outfile)
        output.writeObject(obj)
        print("Object saved to '{0}'".format(filename))
    except Exception as e:
        print("Error: An error occurred while serializing object! ('{0}')".format(e.message))

def q():
    """
    Quit the application
    """
    sys.exit(0)

def clear():
    """
    Clear the screen
    """
    os.system("cls & clear & cls")

import_all(java)
import_all(org)
obj = JavaObject(custom_to_list(deserialized))
globals().update({"available": [serialize, q, clear, import_all]})
vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact(banner="Welcome to JPDeserializer, in order to start type 'obj' or 'available' or even 'help'\n")
