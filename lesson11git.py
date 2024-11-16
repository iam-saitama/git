git config --global user.name # задать имя пользователя
git config --global user.email # добавить почту
git --help # общая докуменация по git
git init # создать пустой репозиторий
git add file.py # добавить файл с указанием имени
git add . # добавить все файлы
git status # проверка статуса репозитория
git commit -m "comment" # однострочное сообщение
git commit # для подробного комментария
git log -p # просмотр историй с изменениями
git diff # просмотр изменений до коммита
git diff --staged # для просмотра подготовленных изменений
git diff file.py # просмотреть изменения внесенные только в этот файл
git show j5k4675mn9kjk # просмотр заданного коммита (указать идентификатор или хэш)
git rm # удаление файла из индекса рабочей копии
git checkout file.py # восстановить файл не подготовленный к коммиту
git reset HEAD # отмена изменений
git revert HEAD # откат последнего коммита (не откатывает к более ранему коммиту)
git branch new_branch_name # создать новую ветку
git branch # просмотр всех веток
gti branch -a # список удаленных веток
git branch -d branch_name # удалить ветку
git branch -D branch_nam # принудительно удалить ветку
git merge branch_name # объедениить две ветки
git merge --abort # прервать слияние