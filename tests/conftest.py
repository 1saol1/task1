import os

os.environ["SECRET_KEY"] = "test-secret-key"
os.environ["DATABASE_URI"] = "sqlite:///:memory:"

import pytest
from task_manager import app, db


@pytest.fixture
def client():
    app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False
    )

    with app.app_context():
        db.create_all()

        yield app.test_client()

        db.session.remove()
        