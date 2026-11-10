# Пошаговое выполнение заданий по Git

Задания варианта 2: **средние №2, №4, №7; повышенные №2, №6**.

## Среднее №2 — создать локальный репозиторий
```bash
git clone git@github.com:basegod812/python-lab-01.git
cd python-lab-01
git status
```
Клонированный репозиторий является локальным Git-репозиторием. Для создания с нуля отдельно можно использовать `git init -b main`.

## Среднее №4 — изменить файл и выполнить второй коммит
Этот репозиторий уже содержит несколько реальных коммитов, сделанных в ходе загрузки файлов.
Демонстрация локально:
```bash
git checkout -b demonstration
# Добавьте осмысленное пояснение в README.md
git add README.md
git commit -m "docs: clarify Git exercise"
git log --oneline -5
```
Не нужно делать пустые фиктивные коммиты.

## Среднее №7 — .gitignore
В корне хранится `.gitignore`. Проверьте игнорирование:
```bash
python -m compileall -q main.py
git status --ignored
```

## Повышенное №2 — SSH для GitHub
Выполнить на своём компьютере, не загружая приватный ключ:
```bash
ssh-keygen -t ed25519 -C "your-github-email@example.com"
```
Скопировать содержимое файла `~/.ssh/id_ed25519.pub` в GitHub → Settings → SSH and GPG keys → New SSH key. Затем проверить:
```bash
ssh -T git@github.com
```
В GitHub публичный ключ разрешён; **приватный ключ никому не отправлять**.

## Повышенное №6 — GitHub Actions
Настроен workflow `.github/workflows/python.yml`; он запускает компиляцию и программу при push/PR.
Проверить выполнение на вкладке Actions репозитория.

## Отправка всех веток и тегов
После локальных изменений:
```bash
git checkout main
git merge demonstration
git push --all origin
git push --tags origin
```
Проверить историю: `git log --oneline --all --graph`.

Примечание: выполнение SSH-настройки и отправки локальных веток невозможно подтвердить одним только наличием файлов в GitHub.
