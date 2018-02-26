from flask import Flask, render_template, json
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
# from wtforms import validators

import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jason' # change this for production, remove this if publishing source code
bootstrap = Bootstrap(app)

@app.route('/tasks')
def tasks():
	url = 'http://localhost:5000/auth'
	payload = {'username': 'jason', 'password': 'jason'}
	headers = {'content-type': 'application/json'}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	token = json.loads(response.text)['access_token']

	url = 'http://localhost:5000/tasks'
	headers = {'content-type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
	
	response = requests.get(url, headers=headers)
	tasks = json.loads(response.text)['tasks']
	return render_template('tasks.html', tasks=tasks)

class PostCategoryForm(FlaskForm):
	category = StringField('Category', validators=[DataRequired(), Length(1, 26)])
	submit = SubmitField('Submit')

@app.route('/categories', methods=['GET', 'POST'])
def categories():
	newCategory = None
	
	form = PostCategoryForm()

	url = 'http://localhost:5000/auth'
	payload = {'username': 'jason', 'password': 'jason'}
	headers = {'content-type': 'application/json'}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	token = json.loads(response.text)['access_token']

	if form.validate_on_submit():
		newCategory = form.category.data
		form.category.data = ''

		url = 'http://localhost:5000/category'
		payload = {'name': newCategory}
		headers = {'content-type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
		
		response = requests.post(url, data=json.dumps(payload), headers=headers)
	
	url = 'http://localhost:5000/categories'
	headers = {'content-type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
	
	response = requests.get(url, headers=headers)
	categories = json.loads(response.text)['categories']
	return render_template('categories.html', categories=categories, form=form)

class PostTaskForm(FlaskForm):
	task = StringField('Title', validators=[DataRequired(), Length(1, 26)])
	category = StringField('Category', validators=[DataRequired(), Length(1, 26)])

	submit = SubmitField('Submit')

@app.route('/category/<_id>', methods=['GET', 'POST'])
def category(_id):
	newTaskTitle = None
	newTaskCategory = None

	form = PostTaskForm()

	url = 'http://localhost:5000/auth'
	payload = {'username': 'jason', 'password': 'jason'}
	headers = {'content-type': 'application/json'}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	token = json.loads(response.text)['access_token']

	if form.validate_on_submit():
		newTaskTitle = form.task.data
		newTaskCategory = form.category.data

		form.task.data = ''
		form.category.data = ''

		url = 'http://localhost:5000/task'
		payload = {'title': newTaskTitle, 'category_name': newTaskCategory}
		headers = {'content-type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
		
		response = requests.post(url, data=json.dumps(payload), headers=headers)

	url = 'http://localhost:5000/category/{}'.format(_id)
	headers = {'content-type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
	
	response = requests.get(url, headers=headers)
	category_tasks = json.loads(response.text)['tasks']
	category_name = json.loads(response.text)['name']	

	return render_template('category.html', category_tasks=category_tasks, category_name=category_name, form=form)

if __name__ == '__main__':
	app.run(debug=True, port=5025)