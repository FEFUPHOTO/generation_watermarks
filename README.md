# Генерация логотипов для постов и водяных знаков

**Структура проекта:**

```
.
├── fonts
|   ├── futurademic.ttf
├── patterns
|   ├── post.png
|   ├── watermark.png
├── result
|   ├── logo_post
|   |   └── post_[ФИО].png
|   └── logo_watermark
|       └── watermark_[ФИО].png
├── main.py
├── input.txt
```

- fonts - хранит в себе шрифт
- patterns - хранит в себе патерны
- win_exe - exe файл для запуска на Windows
- mac_exe - exe файл для запуска на macos

**Структура input.txt:**

```
Петров Петр Петрович
Нестеров Дмитрий Алексеевич
...
или 
Петров Петр
Нестеров Дмитрий
...
```

**запуск кода:**

```shell
 source venv/bin/activate
 pip install -r requirements.txt
 py main.py
```