# Регистрация
def test_register(client):
    response = client.post(
        "/auth/register",
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

# Логин
def test_login(client):
    client.post(
        "/auth/register",
        json={"username": "testuser", "password": "testpass"}
    )
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

# Создание закладки
def test_create_bookmark(client):
    client.post("/auth/register", json={"username": "test", "password": "test"})
    login = client.post("/auth/login", json={"username": "test", "password": "test"})
    token = login.json()["access_token"]

    responce = client.post(
        "/bookmarks/",
        json={
            "url": "https://www.roblox.com/users/5393896161/profile",
            "title": "Profile Roblox"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert responce.status_code == 200
    assert responce.json()["title"] == "Profile Roblox"

# Показать все закладки
def test_get_bookmarks(client):
    client.post("/auth/register", json={"username": "test", "password": "test"})
    login = client.post("/auth/login", json={"username": "test", "password": "test"})
    token = login.json()["access_token"]
    
    response = client.get(
        "/bookmarks/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Поиск закладки по названию
def test_search_bookmark(client):
    client.post("/auth/register", json={"username": "test", "password": "test"})
    login = client.post("/auth/login", json={"username": "test", "password": "test"})
    token = login.json()["access_token"]
    
    client.post(
        "/bookmarks/",
        json={"url": "https://example.com", "title": "Example"},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    response = client.get(
        "/bookmarks/search?bookmark_title=Exam",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1

# Поиск закладки по ID
def test_get_bookmark_id(client):
    client.post("/auth/register", json={"username": "test", "password": "test"})
    login = client.post("/auth/login", json={"username": "test", "password": "test"})
    token = login.json()["access_token"]

    # Создаём закладку
    create = client.post(
        "/bookmarks/",
        json={"url": "https://example.com", "title": "Example"},
        headers={"Authorization": f"Bearer {token}"}
    )
    bookmark_id = create.json()["id"]

    # Получаем её по id
    response = client.get(
        f"/bookmarks/{bookmark_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == bookmark_id