from app import app, db
from flask import render_template, request, flash, get_flashed_messages, redirect, url_for
from datetime import datetime
from app.forms import AddTaskForm, DeleteTaskForm
from app.models import Task


@app.route("/", methods=["GET", "POST"])
def home():
   form = AddTaskForm()
   tasks = None
   if request.form:
      try:
         task = Task(title=form.title.data, date=datetime.utcnow())
         db.session.add(task)
         db.session.commit()
         return redirect(url_for('home'))
      except Exception as e:
         print("Failed to add Task")
         print(e)
   tasks = Task.query.all()
   return render_template('index.html', tasks=tasks)

@app.route("/update", methods=["POST"])
def update():
   try:
      newTask = request.form.get("newTask")
      oldTask = request.form.get("oldTask")
      task = Task.query.filter_by(title=oldTask).first()
      task.title = newTask
      db.session.commit()
   except Exception as e:
      print("Could not update book title")
      print(e)
   return redirect('/')

@app.route("/delete", methods=["POST"])
def delete():
   title = request.form.get('task')
   task = Task.query.filter_by(title=title).first()
   db.session.delete(task)
   db.session.commit()
   return redirect('/')
