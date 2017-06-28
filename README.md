# JPDeserializer
JPDeserializer is Java-Python Object deserializer, it uses Jython to convert a fully serialized object to a browsable python-like object.

## Dependencies
The only dependency is the Jython JAR downloadble frome here http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar

## How to run
The command is pretty easy:
```bash
java -jar jython.jar jpdeserializer.py -obj serialized.object
```
You may need to import custor JAR to class path, this is possible via **-cp** switch like following
```bash
java -jar jython.jar jpdeserializer.py -cp myfaces.jar -obj serialized.object
```

### Example
Below an example of what you should expect:
```bash
java -jar jython.jar jpdeserializer.py -cp myfaces.jar -obj serialized.ser
```
```
Welcome to JPDeserializer, in order to start type 'obj' or 'available' or even 'help'

>>> obj
  <list>
       ┠  [0](TreeStructureManager$TreeStructComponent) => org.apache.myfaces.application.TreeStructureManager$TreeStructComponent@6f94fb9d
       ┠  [1]<list>
       ┃       ┠  [0]<list>
       ┃       ┃       ┠  [0]<list>
       ┃       ┃       ┃       ┠  [0](NoneType) => None
       ┃       ┃       ┃       ┠  [1](NoneType) => None
       ┃       ┃       ┃       ┠  [2](NoneType) => None
       ┃       ┃       ┃       ┠  [3](NoneType) => None
       ┃       ┃       ┃       ┠  [4](NoneType) => None
       ┃       ┃       ┃       ┠  [5](NoneType) => None
       ┃       ┃       ┃       ┠  [6](NoneType) => None
       ┃       ┃       ┠  [1](Locale) => it
       ┃       ┃       ┠  [2](String) => HTML_BASIC
       ┃       ┃       ┠  [3](String) => /jsp/login_notemplate.jsp
       ┃       ┃       ┠  [4](long) => 0
       ┃       ┠  [1](NoneType) => None
       ┃       ┠  [2](ArrayList) => [[Ljava.lang.Object;@20b9d5d5]
       ┠  [2](String) => /jsp/login_notemplate.jsp
>>> obj[1][2]
  (ArrayList) => [[Ljava.lang.Object;@20b9d5d5]
>>> obj[1][2].size()
  (int) => 1
>>> obj[1][2].get(0)
  (array) => array(java.lang.Object, [array(java.lang.Object, [array(java.lang.Object, [u'_idJsp0', None, u'javax.faces.Grid', None, {javax.faces.webapp.UIComponentTag.FORMER_CHILD_IDS: [_idJsp1, main_form], forceIdIndex: true}, None, None]), None, None, u'0', u'0', None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, u'100%']), None, [[Ljava.lang.Object;@291373d3, [Ljava.lang.Object;@372ca2d6]])
>>> obj[1][2].get(0).tolist()
  <list>
       ┠  [0](array) => array(java.lang.Object, [array(java.lang.Object, [u'_idJsp0', None, u'javax.faces.Grid', None, {javax.faces.webapp.UIComponentTag.FORMER_CHILD_IDS: [_idJsp1, main_form], forceIdIndex: true}, None, None]), None, None, u'0', u'0', None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, u'100%'])
       ┠  [1](NoneType) => None
       ┠  [2](ArrayList) => [[Ljava.lang.Object;@291373d3, [Ljava.lang.Object;@372ca2d6]
>>> 
```

It's even possible to modify and then serialize again an object, this is possible via **serialize** function
