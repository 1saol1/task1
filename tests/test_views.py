from task_manager.models import Task


def test_home_page(client):
    response = client.get('/')

    assert response.status_code == 200


def test_no_tasks(client):
    response = client.get('/')

    assert response.status_code == 200

    assert 'Задач пока нет' in response.text


def test_add_task(client):

    data = {'title': "Изучить pytest"}

    response = client.post('/add', data=data)

    task = Task.query.get(1)

    assert data['title'] == task.title
    assert response.status_code == 302


def test_change_task(client):

    task_before_change = {'title': "Изучить pytest"}
    response_add = client.post('/add', data=task_before_change)
    task_after_change = {'title': 'Помыть посуду'}

    response_change = client.post('/change/1', data=task_after_change)

    task = Task.query.get(1)

    assert response_add.status_code == 302
    assert response_change.status_code == 302
    assert task.title == task_after_change['title']


def test_delete_task(client):
    task = {'title': "Изучить pytest"}
    response_add = client.post('/add', data=task)

    response_delete = client.post('/delete/1')

    response_404 = client.get('/1')

    assert response_add.status_code == 302
    assert response_delete.status_code == 302
    assert response_404.status_code == 404


def test_complete_task(client):
    task = {'title': "Изучить pytest"}
    response_add = client.post('/add', data=task)

    response_complete = client.post('/completed/1')

    tsk = Task.query.get(1)

    assert tsk.completed is True
    assert response_add.status_code == 302
    assert response_complete.status_code == 302


def test_task_not_found(client):
    response_get = client.get('/1')

    assert response_get.status_code == 404


def test_empty_file(client):
    task = {}
    response_add = client.post('/add', data=task)

    assert response_add.status_code == 200
    assert Task.query.count() == 0
