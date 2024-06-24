# Blogicum

**Blogicum** - это блоговая платформа, которая позволяет пользователям создавать и публиковать посты, а также просматривать посты других пользователей.


## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/blogicum.git
    cd blogicum
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```
## Автор
[Максим]