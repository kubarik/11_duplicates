# Anti-Duplicator

Скрипт ищет дубликаты в указанной папке, включая подпапки.
Дубликатами считаются файлы с одинаковым именем и размером.

# Как использовать

Импортируемые модули
```python
import os #функции для работы с операционной системой
import sys #доступ к переменным
```

Анализируем папку:
```python
get_dublicate_files(path_to_folder)
```
где
  path_to_folder - путь к папке, в которой нужно найти дубликаты

```bash

Запус и пример ответ
$ python duplicates.py c:\temp\
Magic Retouch Pro v2.3.zxp 821390
Retouch Preset.tpl 90192
info.txt 3143
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
