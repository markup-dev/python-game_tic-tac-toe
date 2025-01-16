# Крестики-нолики (Tic-tac-toe)

## 📝 Описание
Классическая консольная игра "Крестики-нолики" для двух игроков, реализованная на Python. Игроки по очереди ставят на свободные клетки поля 3×3 свои знаки (один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.

## 🚀 Возможности
- Игра для двух игроков
- Ввод имен игроков
- Отображение игрового поля после каждого хода
- Проверка корректности ходов
- Определение победителя
- Сохранение статистики игр
- Просмотр истории сыгранных партий

## 🎮 Как играть
1. Запустите игру командой:
```bash
python tic_tac_toe.py
```
2. Введите имена игроков
3. Делайте ходы по очереди, указывая:
   - Номер строки (1-3)
   - Номер столбца (1-3)
4. Игра завершается при победе одного из игроков или ничьей

## 🎯 Правила игры
- Игроки ходят по очереди
- Первый игрок ходит крестиками (X)
- Второй игрок ходит ноликами (0)
- Для победы нужно собрать три своих символа в ряд:
  - По горизонтали
  - По вертикали
  - По диагонали

## 📊 Статистика
- Игра сохраняет результаты всех партий в файл `statistics.txt`
- Записывается следующая информация:
  - Имена игроков
  - Победитель
  - Длительность партии
- Статистику можно посмотреть в начале и в конце игры

## 🛠 Технические требования
- Python 3.6+
- Стандартные библиотеки Python:
  - datetime

## 📁 Структура проекта
    ├── `tic_tac_toe.py`: Основной файл с реализацией игры
    ├── `statistics.txt`: Файл для хранения статистики игр
    └── README.md # Документация

## 👥 Авторы
markup-dev Кристина
