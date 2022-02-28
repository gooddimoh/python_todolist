from flask import render_template, request, jsonify
from app import app
from app import database as database

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):

    try:
        database.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    data = request.get_json()
    try:
        if "status" in data:
            database.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            database.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    database.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = database.fetch_todo()
    return render_template("index.html", items=items)

@app.route("/generate")
def generate(user_id):
    generator = database.generate(user_id)
    for user in generator:
        print(user)
