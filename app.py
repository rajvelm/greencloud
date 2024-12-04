import ansible_runner
import subprocess
from flask import Flask, render_template, url_for, request, redirect

from datetime import datetime

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/socgen/greencloud/sampleApp2/test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')
    # if request.method == 'POST':
    #     task_content = request.form['content']
    #     new_task = Todo(content=task_content)

        # try:
            # db.session.add(new_task)
            # db.session.commit()
            # return redirect('/')
        # except:
        #     return 'There was an issue adding your task'
        # finally:
            # db.session.close()

    # else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        # return render_template('index.html', tasks=tasks)


# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)
#
#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'
#     finally:
#         db.session.close()

@app.route('/go', methods=['GET', 'POST'])
def go():

    inventory_file = '/etc/ansible/hosts'
    playbook_file = '/home/socgen/greencloud/sampleApp2/installJava.yml'

    r = ansible_runner.run(
        playbook=playbook_file,
        inventory=inventory_file)



    return render_template('index.html', status=r.status, rc = r.rc, stats=r.stats)



if __name__ == "__main__":
    app.run(debug=True)
