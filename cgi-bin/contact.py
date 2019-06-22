#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cgi

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>send message</title>
<style>
h1 {
font-size: 3em;
}
</style>
</head>
<body>
<p>Name</p>
<p>%s</p>
<p>E-mail</p>
<p>%s</p>
<p>Date</p>
<p>%s</p>
<p>Message</p>
<p>%s</p>
</body>
</html>
"""

form = cgi.FieldStorage()
Nametext = form.getvalue('yourName','')
Emailtext = form.getvalue('yourEmail','')
Datetext = form.getvalue('inputDate','')
Messagetext = form.getvalue('yourMessage','')


print(html_body % (Nametext,Emailtext,Datetext,Messagetext))
