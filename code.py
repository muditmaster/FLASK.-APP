from flask import Flask,jsonify, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"


tasks = [
    {
        'id' : 1,
        'name' : u'chuck',
        'contact': u'1607748412',
        'done' : False
    },

    {
        'id' : 2,
        'name' : u'trance',
        'contact' : u'1599882277',
        'done' : False
    }

]

@app.route('/add-data', methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status" :'error',
            "message" : 'Please provide the data!'
        },400)
    task = {

        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': True
    }

    tasks.append(task)
    return jsonify({
            "status" :'success',
            "message" : 'task added successfully'
        })



@app.route('/get-data')
def get_task():
    return jsonify({
        "data" : tasks
    })

if __name__ == '__main__':
    app.run()
