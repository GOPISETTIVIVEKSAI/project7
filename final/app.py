from flask import Flask,render_template,request
import pymysql as sql
my_connection=sql.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='final'
)
my_cursor=my_connection.cursor()
app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')
@app.route('/admission',methods=['GET'])
def admissionpage():
    return render_template('admission.html')
@app.route('/GOBACK',methods=['GET'])
def GOBACK():
    return render_template('index.html')


@app.route('/Register',methods=['GET'])
def register():
    return render_template('Register.html')
@app.route('/register-form',methods=['POST'])
def registerdata():
    id=request.form['id']
    name=request.form['First Name']
    email=request.form['Email']
    phone=request.form['phone']
    percentage=request.form['percentage']
    rank=request.form['rank']
    course=request.form['course']
    address=request.form['Address']
    query='''
        insert into student(id,`name`,Email,phone,percentage,`rank`,course,address)
        values(%s,%s,%s,%s,%s,%s,%s,%s);
    '''
    values=(id,name,email,phone,percentage,rank,course,address)
    my_cursor.execute(query,values)
    my_connection.commit()
    return  render_template('Register.html',context="data inserted")



@app.route('/view',methods=['GET'])
def view():
    query='''
        select * from student;
    '''
    my_cursor.execute(query)
    data=my_cursor.fetchall()
    return render_template('view.html',details=data)


@app.route('/update',methods=['GET'])
def update():
    return render_template('update.html')
@app.route('/update-form',methods=['post'])
def update_form():
    _id =request.form['id']
    field=request.form['field']
    new_value=request.form['new_value']
    query=f'''
        update student
        set {field}='{new_value}'
        where id= {_id};
    '''
    my_cursor.execute(query)
    my_connection.commit()
    return  render_template('update.html',context="data updated")

@app.route('/delete',methods=['GET'])
def delete():
    return render_template('delete.html')
@app.route('/delete-form',methods=['POST'])
def deletedata():
    _id =request.form['id']
    query=f'''
        delete from student
        where id=%s;  
    '''
    values=(_id)
    my_cursor.execute(query,values)
    my_connection.commit()
    return render_template('delete.html',context="data has been deleted")




@app.route('/call-form',methods=['POST'])
def calldata():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    course=request.form['course']
    query='''
        insert into callme(`name`,Email,phone,course)
        values(%s,%s,%s,%s);
    '''
    values=(name,email,phone,course)
    my_cursor.execute(query,values)
    my_connection.commit()
    return  render_template('index.html')
app.run()
