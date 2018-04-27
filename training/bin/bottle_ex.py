#!/bin/python3.6
import bottle
app=bottle.Bottle()
@app.route('/')
def homepage():
  return 'Welcome Page, Hello Mohan'
#app.run()
@app.route('/hello')
def hellopage():
  return 'Hello Page'

@app.route('/xyz/<name>') ## pass the input in browser http://localhost/xyz/yourinput, if passwd mohan will return Hellomohan
def msg(name):
  return "Hello" + name
#app.run(host='172.31.35.243',port=80)

@app.route('/login') #/login provides user field and submit button
def loginpage():
  return ''' <form action='/login1' method='post' > 
	     user: <input type=text name='username' />
             <input type=submit value=submit />
	     </form>
	 ''' 
@app.post('/login1') ## method to accept input
def login():
  r=bottle.request.forms.get('username')
  return 'Hello' + r

@app.route('/querydb')
def queryDB():
  import sqlite3
  con=sqlite3.connect('my_db')
  cur=con.cursor()
  cur.execute('select * from log_data')
  r=cur.fetchall()
  return str(r)

s='''<table>'''
for i,j in r:
  s=s+'<tr>'+'<td>'+str(i)+'<td>'+'<td>'+str(j)+'<td>'+'</tr>'
  s+='</table>'
return s

app.run(host='172.31.35.243',port=80)
