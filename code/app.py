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

if __name__ == '__main__':
	app.run(debug=True, port=5025)