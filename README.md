# Anti-Duplicator

Скрипт ищет дубликаты в указанной папке, включая подпапки.
Дубликатами считаются файлы с одинаковым именем и размером.

# Как использовать

Импортируемые модули
```python
from collections import defaultdict
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
c:\temp\Magic Retouch\Magic Retouch Pro\Plug-In\Photoshop CS5\Magic Retouch Pro v2.3.zxp 821390
c:\temp\Magic Retouch Pro\Magic Retouch Pro\Retouch Preset\Retouch Preset.tpl 90192
c:\temp\Баннер\info.txt 3143
```


