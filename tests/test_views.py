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

