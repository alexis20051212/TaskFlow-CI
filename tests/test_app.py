
from app import create_app


def test_home_page():
    app = create_app()
    app.config["TESTING"] = True

    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"TaskFlow CI" in response.data


def test_add_task():
    app = create_app()
    app.config["TESTING"] = True

    client = app.test_client()

    response = client.post(
        "/add",
        data={"task": "Complete homework"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Complete homework" in response.data


def test_empty_task():
    app = create_app()
    app.config["TESTING"] = True

    client = app.test_client()

    response = client.post(
        "/add",
        data={"task": "   "},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"No hay tareas registradas." in response.data