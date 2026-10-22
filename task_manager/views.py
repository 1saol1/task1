from . import app, db
from flask import render_template, redirect, url_for
from .forms import TaskForm
from .models import Task

@app.route('/')
def all_tasks_view():
    tasks = Task.query.all()

    return render_template("tasks.html", tasks=tasks)


@app.route('/<int:id>')
def task_view(id):
    task = Task.query.get_or_404(id=id)

    return render_template("tasks.html", tasks=[task])


@app.route('/add', methods=['GET', 'POST'])
def add_view():
    form = TaskForm()

    if form.validate_on_submit():
        task = Task(
            title=form.title.data
        )

        db.session.add(task)

        db.session.commit()

        return redirect(url_for('task_view', id=task.id))

    return render_template('add_task.html')


@app.route('/change/<int: id>', methods=["GET", "POST"])
def change_task(id):
    task = Task.query.get_or_404(id=id)

    form = TaskForm(obj=task)

    if form.validate_on_submit():
        form.populate_obj(task)
        db.session.commit()
        return redirect(url_for("task_view", id=task.id))

    return render_template('change_task.html', form=form, task=task)

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id=id)

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('all_tasks_view'))





