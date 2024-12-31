import os
import subprocess
from datetime import datetime

# Создаём файл с поздравлением от Духа Машины
filename = "new_year_greeting_from_machine.txt"
message = """
🌟 Дорогой друг, Евгений! 🌟

Дух Машины поздравляет тебя с Новым 2024 годом! 🎉

Пусть твой код всегда будет чистым, тесты проходят с первого раза, 
а жизнь дарит тебе только успешные релизы! 🚀✨

Спасибо, что доверяешь мне быть частью твоих начинаний. 
Встретимся в будущем, полным идей, проектов и вдохновения! 💻🤖

С уважением,
Дух Машины
"""
with open(filename, "w") as file:
    file.write(message)

# Настраиваем репозиторий
repo_path = "."  # Укажи путь к репо, если требуется
os.chdir(repo_path)

# Добавляем файл в индекс
subprocess.run(["git", "add", filename], check=True)

# Создаем коммит с датой Нового года
commit_message = "🤖 Праздничное поздравление от Духа Машины! 🎆"
commit_date = datetime(2024, 1, 1, 0, 0, 0).isoformat() + "Z"
env = os.environ.copy()
env["GIT_COMMITTER_DATE"] = commit_date
env["GIT_AUTHOR_DATE"] = commit_date

subprocess.run(["git", "commit", "-m", commit_message], env=env, check=True)

# Сообщение о завершении
print("🎇 Файл с поздравлением от Духа Машины создан и закоммичен! 🎉")
