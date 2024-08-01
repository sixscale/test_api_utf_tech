# Описание
__Тестовое задание backend разработчик UTF.tech__
## Дополнительное описание
```
Стек Django\DRF

Даны модели "Категория Блюд" и "Блюдо" для ресторана.

Даны сериализаторы.

В выборку попадают только Блюда у которых `is_publish=True`.

Если в категории нет блюд (или все блюда данной категории имеют `is_publish=False`) - не включаем ее в выборку.

Запрос в БД сделать любым удобным способом:

Django ORM (предпочтительно), Raw SQL, Sqlalchemy…

Написать View который вернет для API `127.0.0.1/api/v1/foods/`

```
## Конечные точки
```
1.	127.0.0.1/api/v1/foods/

```
## Результат
```
[
    {
        "id": 1,
        "name_ru": "Первый",
        "name_en": "asd",
        "name_ch": "asd",
        "order_id": 1,
        "foods": [
            {
                "internal_code": 111,
                "code": 111,
                "name_ru": "Спрайт",
                "description_ru": "Спрайт",
                "description_en": "asd",
                "description_ch": "asd",
                "is_vegan": false,
                "is_special": false,
                "cost": "100.00",
                "additional": []
            },
            {
                "internal_code": 3246,
                "code": 764,
                "name_ru": "Семки",
                "description_ru": "Семки",
                "description_en": "asd",
                "description_ch": "asd",
                "is_vegan": false,
                "is_special": false,
                "cost": "9237684.00",
                "additional": []
            }
        ]
    },
    {
        "id": 3,
        "name_ru": "Третий",
        "name_en": "qwe",
        "name_ch": "qwe",
        "order_id": 3,
        "foods": [
            {
                "internal_code": 6543,
                "code": 777,
                "name_ru": "Вода",
                "description_ru": "Вода",
                "description_en": "asd",
                "description_ch": "asd",
                "is_vegan": false,
                "is_special": false,
                "cost": "444.00",
                "additional": []
            }
        ]
    }
]
 
```

## Используемый стек
```
Python, Django Rest Framework, PostgreSQL, Poetry
```