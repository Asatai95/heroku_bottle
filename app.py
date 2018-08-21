import MySQLdb
import os
from bottle import route, run, template, static_file, request, redirect, response, view

# db_name = {'heroku'}
# host = {'us-cdbr-iron-east-01.cleardb.net'}
# username = {'b8b921e229e863'}
# passwd = {'a87b2e7e'}

# connection = mysql.createConnection({
#   host     : 'us-cdbr-iron-east-01.cleardb.net',
#   user     : 'b4da42a09cc349',
#   password : 'dd235253',
#   database : 'heroku'
# });


@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@route("/")
def top():

    return template('top')

@route("/test")
@view("test")
def top_db():

    db = MySQLdb.connect(db='heroku_d9c662866ce227f', host='us-cdbr-iron-east-01.cleardb.net', port=3306, user='b4da42a09cc349', passwd='dd235253')
    con = db.cursor()

    sql = 'select id, test from test where id = 1'
    test = con.execute(sql)
    db.commit()
    print(sql)
    print(test)

    result = con.fetchall()
    result = result[0][1]
    print(result)

    return dict(sub = result)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
