#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
if form.getvalue("submit"):
	gpio = open("/dev/pigpio", 'a')
	gpio.write("w 4 1 mils 1000 w 4 0\n")
	gpio.close()

print ("""Content-Type: text/html\n
<html>
  <body>
    <form action="garage.py" method="POST">
      <div style="text-align:center;margin-top:20%">
        <input type="submit" value="Open / Close" name="submit" style="font-size:500%;padding:50px;" />
      </div>
    </form>
  </body>
</html>
""")
