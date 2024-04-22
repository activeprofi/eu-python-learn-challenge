from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users = {}

        @app.post("/user")
        def create_user():
            data = request.get_json()

            if "name" not in data:
                return {"errors": {"name": "This field is required"}}, 422

            username = data["name"]
            users[username] = {}
            return {"data": f"User {username} is created!"}, 201

        @app.get("/user/<name>")
        def get_user(name):
            if name not in users:
                return "errors", 404

            return {"data": f"My name is {name}"}

        @app.patch("/user/<name>")
        def update_user(name):
            temp_user = users[name]
            data = request.get_json()
            new_user_name = data["name"]

            del users[name]
            users[new_user_name] = temp_user

            return {"data": f"My name is {new_user_name}"}

        @app.delete("/user/<name>")
        def delete_user(name):
            del users[name]
            return "success", 204
