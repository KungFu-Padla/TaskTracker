# TaskTracker — система управления личными задачами

Курсовой проект, выполняемый в рамках лабораторных работ № 2, 3, 5, 6, 7, 8.

## Описание
TaskTracker позволяет пользователю:
- регистрироваться/авторизовываться;
- создавать, просматривать, редактировать и удалять задачи;
- помечать задачи как выполненные;
- фильтровать задачи по статусу (активные / выполненные / все).

## Стек
- Язык: Python 3
- Веб-фреймворк: Flask
- Тесты: pytest
- CI: GitHub Actions
- Интерфейс: Figma (макеты)
- Установщик: Inno Setup / Setup Creator

## Структура репозитория
```
TaskTracker/
├── .github/workflows/ci.yml      # GitHub Actions (ЛР 3, 7)
├── app.py                        # Прототип приложения (ЛР 7)
├── tests/
│   ├── test_app.py               # Тесты проекта (ЛР 7)
│   └── test_simple.py            # Простые тесты (деление на ноль, чёт/нечёт) (ЛР 3)
├── requirements.txt
├── docs/
│   ├── lab2_git_flow.md          # ЛР 2: Git / GitFlow / GitHub
│   ├── lab3_ci.md                # ЛР 3: GitHub Actions
│   ├── lab5_architecture/        # ЛР 5: диаграммы архитектуры (PlantUML)
│   │   ├── use_case.puml
│   │   ├── sequence.puml
│   │   ├── state.puml
│   │   ├── class.puml
│   │   └── deployment.puml
│   ├── lab6_figma.md             # ЛР 6: макеты интерфейса (Figma)
│   └── lab8_setup.md             # ЛР 8: установочный пакет
├── setup/
│   └── install.iss               # Скрипт Inno Setup (ЛР 8)
└── Отчет_по_ЛР.docx              # Итоговый отчёт
```

## Запуск прототипа
```bash
pip install -r requirements.txt
python app.py
```
Приложение будет доступно по адресу http://127.0.0.1:5000

## Запуск тестов
```bash
pytest
```
