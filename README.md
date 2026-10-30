# Task Manager (Менеджер задач)

Простое веб-приложение для управления списком задач, написанное на Flask.

## Возможности
- Добавление новых задач
- Редактирование названий
- Отметка задач как выполненных
- Удаление задач

## Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/ваш-username/ваш-репозиторий.git
   cd ваш-репозиторий
   ```

2. **Создайте и активируйте виртуальное окружение:**
    bash
    python -m venv venv
    # Для Windows:
    venv\Scripts\activate
    # Для macOS/Linux:
    source venv/bin/activate

3. **Установите зависимости:**
    bash
    pip install -r requirements.txt

4. **Настройте переменные окружения:**
    Скопируйте файл .env.example в .env:
    bash
    cp .env.example .env
    Откройте .env и замените your-secret-key-here на любую случайную строку

5. **Установка базы данных**
    Открыть терминал в корне проекта и выполнить:

   ```bash
   python -m flask --app task_manager shell
   ```
   В открывшейся Python-консоли выполнить:
   ```
   db.create_all()
   ```
   Выйти из консоли с помощью exit()


6. **Запустите приложение:**
    ```bash
    flask run
    ```