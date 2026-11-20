# Лабораторная работа № 2. Git, GitHub Desktop, GitHub (GitFlow)

**Цель:** на командном уровне отработать ветвление по модели GitFlow на локальном репозитории, связать его с удалённым репозиторием на GitHub и оформить документацию (Wiki) со ссылкой на макет Figma.

## Инструменты
- Git (command line)
- GitHub Desktop
- GitHub (удалённый репозиторий + Wiki)
- Локальный репозиторий проекта TaskTracker

## Пошаговое выполнение

### Шаг 1. Инициализация локального репозитория
```
cd E:\Береснева\TaskTracker
git init
git add .
git commit -m "init: структура проекта TaskTracker"
```

### Шаг 2. Ветвление по GitFlow
Модель GitFlow предусматривает основные ветки:
- `main` (ранее `master`) — релизное состояние, стабильная версия;
- `develop` — ветка разработки, здесь накапливаются изменения;
- `feature/*` — ветки для отдельных возможностей;
- `release/*` — подготовка релиза;
- `hotfix/*` — экстренные исправления.

Выполнение:
```
git branch develop
git checkout develop
git push -u origin develop   # после привязки удалённого репозитория
```

Создание фича-ветки для новой возможности (например, прототип приложения):
```
git checkout -b feature/prototype develop
# ... внесение изменений ...
git add .
git commit -m "feat: добавлен прототип TaskTracker"
git checkout develop
git merge --no-ff feature/prototype
git branch -d feature/prototype
```

### Шаг 3. Работа с GitHub Desktop
1. Установить GitHub Desktop и войти в аккаунт GitHub.
2. `File → Add local repository` → выбрать папку `E:\Береснева\TaskTracker`.
3. Создать удалённый репозиторий на GitHub (`TaskTracker`, публичный, без инициализации README, чтобы не было конфликтов).
4. В GitHub Desktop: `Publish repository` → ввести имя репозитория → опубликовать.
5. Отвязать/привязать ветки: локальные `main` и `develop` отправить на удалённый репозиторий (`Push origin`).

### Шаг 4. Создание удалённого репозитория и Wiki
1. На GitHub создать репозиторий `TaskTracker`.
2. В репозитории перейти во вкладку **Wiki** → создать первую страницу `Home`.
3. На странице Wiki разместить ссылку на макет в Figma (см. ЛР 6), например:
   ```
   [Макеты интерфейса TaskTracker (Figma)](https://www.figma.com/... )
   ```
4. Зафиксировать в Wiki краткое описание проекта и инструкцию по развёртыванию.

### Шаг 5. Pull Request (командное взаимодействие)
1. Создать ветку `feature/readme` от `develop`, обновить `README.md`.
2. Запушить ветку в удалённый репозиторий.
3. На GitHub создать Pull Request из `feature/readme` → `develop`.
4. Добавить комментарий (ревью), затем слить (merge) и удалить ветку.

## Итоговые артефакты
- Локальный репозиторий со складами: `main`, `develop`, несколько `feature/*` веток.
- История коммитов (`git log --oneline --graph`).
- Удалённый репозиторий на GitHub со всеми ветками.
- Wiki-страница со ссылкой на Figma.
- Один и более закрытых Pull Request.

## Контрольные вопросы
1. В чём разница между `main` и `develop` в GitFlow?
2. Зачем нужен `--no-ff` при слиянии фича-ветки?
3. Как GitHub Desktop упрощает работу с удалённым репозиторием?
4. Зачем в Wiki нужна ссылка на проект Figma?
