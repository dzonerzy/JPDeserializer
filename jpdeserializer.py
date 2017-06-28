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
import base64
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

def import_all():
    imported_elements = 0
    imports = {
        "java.io": ["Closeable","DataInput","DataOutput", "Externalizable", "FileFilter", "FilenameFilter", "Flushable", "ObjectInput", "ObjectInputValidation", "ObjectOutput", "ObjectStreamConstants", "Serializable","BufferedInputStream","BufferedOutputStream","BufferedReader","BufferedWriter","ByteArrayInputStream","ByteArrayOutputStream","CharArrayReader","CharArrayWriter","Console","DataInputStream","DataOutputStream","File","FileDescriptor","FileInputStream","FileOutputStream","FilePermission","FileReader","FileWriter","FilterInputStream","FilterOutputStream","FilterReader","FilterWriter","InputStream","InputStreamReader","LineNumberInputStream","LineNumberReader","ObjectInputStream","ObjectInputStream.GetField","ObjectOutputStream","ObjectOutputStream.PutField","ObjectStreamClass","ObjectStreamField","OutputStream","OutputStreamWriter","PipedInputStream","PipedOutputStream","PipedReader","PipedWriter","PrintStream","PrintWriter","PushbackInputStream","PushbackReader","RandomAccessFile","Reader","SequenceInputStream","SerializablePermission","StreamTokenizer","StringBufferInputStream","StringReader","StringWriter","Writer","CharConversionException","EOFException", "FileNotFoundException", "InterruptedIOException", "InvalidClassException", "InvalidObjectException", "IOException", "NotActiveException", "NotSerializableException", "ObjectStreamException", "OptionalDataException", "StreamCorruptedException", "SyncFailedException", "UnsupportedEncodingException","UTFDataFormatException", "WriteAbortedException", "IOError"],
        "java.lang": ["Appendable","AutoCloseable","CharSequence","Cloneable","Comparable","Iterable","Readable","Runnable","Thread.UncaughtExceptionHandler","Boolean","Byte","Character","Character.Subset","Character.UnicodeBlock","Class","ClassLoader","ClassValue","Compiler","Double","Enum","Float","InheritableThreadLocal","Integer","Long","Math","Number","Object","Package","Process","ProcessBuilder","ProcessBuilder.Redirect","Runtime","RuntimePermission","SecurityManager","Short","StackTraceElement","StrictMath","String","StringBuffer","StringBuilder","System","Thread","ThreadGroup","ThreadLocal","Throwable","Void","ArithmeticException","ArrayIndexOutOfBoundsException","ArrayStoreException","ClassCastException","ClassNotFoundException","CloneNotSupportedException","EnumConstantNotPresentException","Exception","IllegalAccessException","IllegalArgumentException","IllegalMonitorStateException","IllegalStateException","IllegalThreadStateException","IndexOutOfBoundsException","InstantiationException","InterruptedException","NegativeArraySizeException","NoSuchFieldException","NoSuchMethodException","NullPointerException","NumberFormatException","ReflectiveOperationException","RuntimeException","SecurityException","StringIndexOutOfBoundsException","TypeNotPresentException","UnsupportedOperationException","AbstractMethodError","AssertionError","BootstrapMethodError","ClassCircularityError","ClassFormatError","Error","ExceptionInInitializerError","IllegalAccessError","IncompatibleClassChangeError","InstantiationError","InternalError","LinkageError","NoClassDefFoundError","NoSuchFieldError","NoSuchMethodError","OutOfMemoryError","StackOverflowError","ThreadDeath","UnknownError","UnsatisfiedLinkError","UnsupportedClassVersionError","VerifyError","VirtualMachineError"],
        "java.nio": ["Buffer","ByteBuffer","ByteOrder","CharBuffer","DoubleBuffer","FloatBuffer","IntBuffer","LongBuffer","MappedByteBuffer","ShortBuffer","BufferOverflowException","BufferUnderflowException","InvalidMarkException","ReadOnlyBufferException"],
        "java.util": ["Base64","Collection","Comparator","Deque","Enumeration","EventListener","Formattable","Iterator","List","ListIterator","Map","Map.Entry","NavigableMap","NavigableSet","Observer","Queue","RandomAccess","Set","SortedMap","SortedSet","AbstractCollection","AbstractList","AbstractMap","AbstractMap.SimpleEntry","AbstractMap.SimpleImmutableEntry","AbstractQueue","AbstractSequentialList","AbstractSet","ArrayDeque","ArrayList","Arrays","BitSet","Calendar","Collections","Currency","Date","Dictionary","EnumMap","EnumSet","EventListenerProxy","EventObject","FormattableFlags","Formatter","GregorianCalendar","HashMap","HashSet","Hashtable","IdentityHashMap","LinkedHashMap","LinkedHashSet","LinkedList","ListResourceBundle","Locale","Locale.Builder","Objects","Observable","PriorityQueue","Properties","PropertyPermission","PropertyResourceBundle","Random","ResourceBundle","ResourceBundle.Control","Scanner","ServiceLoader","SimpleTimeZone","Stack","StringTokenizer","Timer","TimerTask","TimeZone","TreeMap","TreeSet","UUID","Vector","WeakHashMap","ConcurrentModificationException","DuplicateFormatFlagsException","EmptyStackException","FormatFlagsConversionMismatchException","FormatterClosedException","IllegalFormatCodePointException","IllegalFormatConversionException","IllegalFormatException","IllegalFormatFlagsException","IllegalFormatPrecisionException","IllegalFormatWidthException","IllformedLocaleException","InputMismatchException","InvalidPropertiesFormatException","MissingFormatArgumentException","MissingFormatWidthException","MissingResourceException","NoSuchElementException","TooManyListenersException","UnknownFormatConversionException","UnknownFormatFlagsException","ServiceConfigurationError"],
        "java.net": ["ContentHandlerFactory","CookiePolicy","CookieStore","DatagramSocketImplFactory","FileNameMap","ProtocolFamily","SocketImplFactory","SocketOption","SocketOptions","URLStreamHandlerFactory","Authenticator","CacheRequest","CacheResponse","ContentHandler","CookieHandler","CookieManager","DatagramPacket","DatagramSocket","DatagramSocketImpl","HttpCookie","HttpURLConnection","IDN","Inet4Address","Inet6Address","InetAddress","InetSocketAddress","InterfaceAddress","JarURLConnection","MulticastSocket","NetPermission","NetworkInterface","PasswordAuthentication","Proxy","ProxySelector","ResponseCache","SecureCacheResponse","ServerSocket","Socket","SocketAddress","SocketImpl","SocketPermission","StandardSocketOptions","URI","URL","URLClassLoader","URLConnection","URLDecoder","URLEncoder","URLStreamHandler","BindException","ConnectException","HttpRetryException","MalformedURLException","NoRouteToHostException","PortUnreachableException","ProtocolException","SocketException","SocketTimeoutException","UnknownHostException","UnknownServiceException","URISyntaxException"],
    }
    for k in imports.keys():
        for element in imports[k]:
            try:
                clazz = __import__('{0}.{1}'.format(k, element), globals(), locals(), ['object'], -1)
                globals().update({str(element): clazz})
                imported_elements += 1
            except ImportError:
                pass
            except Exception:
                pass
    print("[+] Imported {0} classes".format(imported_elements))

def custom_to_list(obj):
    try:
        for i in range(0, len(obj)):
            if type(obj[i]) == array.array:
                obj[i] == obj[i].tolist()
                obj[i] = custom_to_list(obj[i])
        if type(obj) == array.array:
            return obj.tolist()
        else:
            return obj
    except:
        return obj

class Graph(object):
    """
    Represent our Java deserialized object
    """
    @staticmethod
    def show_graph(obj, last_len=0, called=0, prefix=""):

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
                Graph.show_graph(obj[index], last_len, called=called+1, prefix=str(index))
        else:
            if type(obj) in [unicode]:
                print u"{0}  {1}(String) => {2}".format(len_2_graph(last_len, called), "[{0}]".format(prefix) if prefix else "", obj)
            else:
                print u"{0}  {1}({2}) => {3}".format(len_2_graph(last_len, called), "[{0}]".format(prefix) if prefix else "", type(obj).__name__, obj)

def b64(obj):
    """
    Convert an object to its Base64 representation

    :param obj: The object to convert
    :returns: This method return a string (the base64 representation of the object)
    """
    baos = ByteArrayOutputStream()
    oos = ObjectOutputStream( baos )
    oos.writeObject(obj)
    oos.close()
    return Base64.getEncoder().encodeToString(baos.toByteArray())

def serialize(obj, filename):
    """
    Serialize an object and save it to filename

    :param obj: The object to serialize
    :param filename: This is the file whereto save object
    :returns: This method return null
    """
    try:
        outfile = FileOutputStream(filename)
        output = ObjectOutputStream(outfile)
        output.writeObject(obj)
        print("Object saved to '{0}'".format(filename))
    except Exception as e:
        print("Error: An error occurred while serializing object! ('{0}')".format(e.message))

def q():
    """
    Quit the interactive console

    :returns: This method return null and exit with exitcode 0
    """
    sys.exit(0)

def clear():
    """
    Clear the screen

    :returns: This method return null
    """
    os.system("cls & clear & cls")

import_all()
sys.displayhook = Graph.show_graph
obj = custom_to_list(deserialized)
globals().update({"available": [serialize, q, clear, b64]})
vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact(banner="Welcome to JPDeserializer, in order to start type 'obj' or 'available' or even 'help'\n")
