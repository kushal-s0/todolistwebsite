from flask import Flask,request,redirect,render_template,url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template("index.html", todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    new_todo=request.form.get('todo')
    if new_todo:
        todos.append({'text':new_todo,'completed':False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_index>')
def toggle_todo(todo_index):
    todos[todo_index]["completed"] = not todos[todo_index]["completed"]
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_index>')
def delete_todo(todo_index):
    todos.pop(todo_index)
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)