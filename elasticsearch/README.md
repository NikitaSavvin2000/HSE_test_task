Установлен Elasticsearch загружены тестовые данные

Для загрузки данных из google spreadsheet используется файл connect

Для получения данных из elasticsearch используется файл recive результаты сохраняются в файл elasticsearch_data.xlsx
в директорию result

1. Ссылка на установку Elasticsearch - https://www.elastic.co/downloads/elasticsearch
2. Туториал к установке - https://www.youtube.com/watch?v=w3S7mgFsC7U&t=493s

Проблемы:

Не запускался elasticsearch на localhost:9200

Решение:

В директории elasticsearch-8.10.0/config/elasticsearch.yml нужно выставить настройку xpack.security.enabled: false
