#!/usr/bin/python3
import io
import sys
import cgi
import cgitb
cgitb.enable()
sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')              
sys.stderr = io.TextIOWrapper(sys.stderr.buffer,encoding='utf-8')   
 
form=cgi.FieldStorage()
username = form.getvalue('yourName')
email = form.getvalue('yourEmail')
inputdate = form.getvalue('inputDate')
yourmessage = form.getvalue('yourMessage')
html = '''Content-Type: text/html
 
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<style>
body { background-color: cyan; }
</style>
<title>初めてのpython3CGI</title>
<meta name="description" content="">
<meta name="keywords" content="">
</head>
<body>
<header>
<h1 id="titlename">初めてのpython3CGI</h1>
</header>
<div id="contents">
<article>
<section id="top" style="display:block">
<div>
'''
html = html + '名前='+username+' mail='+email 
html = html + '''
</div>
</section>
</article>
</div>
<footer>
</footer>
</body>
</html>
'''
print(html)