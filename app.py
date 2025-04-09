# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(150), unique=True, nullable=False)
	password = db.Column(db.String(150), nullable=False)

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task_name = db.Column(db.String(200), nullable=False)
	category = db.Column(db.String(100))
	due_date = db.Column(db.String(20))
	status = db.Column(db.String(20), default='Pending')
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref=db.backref('tasks', lazy=True))

@app.route('/')
def index():
	tasks = Task.query.all()
	return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
	task_name = request.form.get('task_name')
	category = request.form.get('category')
	due_date = request.form.get('due_date')
	
	new_task = Task(task_name=task_name, category=category, due_date=due_date, status='Pending', user_id=1)
	db.session.add(new_task)
	db.session.commit()
	
	return redirect(url_for('index'))

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
	task = Task.query.get_or_404(task_id)
	
	if request.method == 'POST':
		task.task_name = request.form['task_name']
		task.category = request.form['category']
		task.due_date = request.form['due_date']
		task.status = request.form['status']
		db.session.commit()
		return redirect(url_for('index'))
	
	return render_template('edit_task.html', task=task)

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
	task = Task.query.get_or_404(task_id)
	db.session.delete(task)
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
