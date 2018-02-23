from flask import Flask, render_template, json
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
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

@app.route('/categories')
def categories():
	url = 'http://localhost:5000/auth'
	payload = {'username': 'jason', 'password': 'jason'}
	headers = {'content-type': 'application/json'}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	token = json.loads(response.text)['access_token']

	url = 'http://localhost:5000/categories'
	headers = {'content-type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
	
	response = requests.get(url, headers=headers)
	categories = json.loads(response.text)['categories']
	return render_template('categories.html', categories=categories)

@app.route('/category/<_id>')
def category(_id):
	url = 'http://localhost:5000/auth'
	payload = {'username': 'jason', 'password': 'jason'}
	headers = {'content-type': 'application/json'}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	token = json.loads(response.text)['access_token']

	url = 'http://localhost:5000/category/{}'.format(_id)
	headers = {'content-type': 'application/json', 'Authorization': 'JWT {}'.format(token)}
	
	response = requests.get(url, headers=headers)
	category_tasks = json.loads(response.text)['tasks']
	category_name = json.loads(response.text)['name']
	return render_template('category.html', category_tasks=category_tasks, category_name=category_name)

if __name__ == '__main__':
	app.run(debug=True, port=5025)