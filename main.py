from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:abc123@localhost/tododatabase'
db = SQLAlchemy(app)
class tasks(db.Model):
    sr = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)

@app.route('/',methods=['Get','Post'])
def contacts():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        title = request.form.get('title')
        desc = request.form.get('description')
        if(title!="" or desc!=""):
            record = tasks(title=title, description=desc)
            db.session.add(record)
            db.session.commit()
    return render_template('form.html')
@app.route('/output/',methods=['Get','Post'])
def output():
    # return render_template('output.html')
    try:
        table_content= db.session.query(tasks)
        lists=[]
        count=0
        for row in table_content:
            list=[]
            list.append(row.sr)
            list.append(row.title)
            list.append(row.description)
            lists.append(list)
            count=count+1

        string=""
        for i in range(len(lists)):
            var=""
            for j in range(len(lists[i])):
                var=var+"<td>"+str(lists[i][j])+"</td>"
            string=string+"<tr>"+var+"</tr>"
        string1 = "<html><head><h1>All To Do List Task</h1></head><body><table border=1 cellspacing=0>" \
                  "<tr><th>sr</th><th>Title</th><th>Description</th></tr>" + string + "</table></body></html>"

        return string1
    except Exception as error:
        print("Failed to display Record  from tasks : {}".format(error))




if __name__ == '__main__':
    app.run(debug=True)


