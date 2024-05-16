# **Test_Task_Sarafan**


## **Содержание**

* #### Инструкция по запуску проекта
* #### Выполненные задачи
* #### Документация к API


### **Инструкция по запуску проекта**


#### Клонировать репозиторий:

```
git clone git@github.com:qtafy23/Test_Task_Sarafan.git
```

#### Создать вирутальное окружение и файл .env, установить зависимости

```
python -m venv venv

touch .env
```

##### Заполнить файл данными по примеру `env.example`

```
source venv/scripts/activate

pip install -r requirements.txt
```

#### Создать миграции и запустить сервер!

```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```


### **Выполненные задачи**


1. [x] Реализовать Django проект магазина продуктов со следующим функционалом:
2. [x] Должна быть реализована возможность создания, редактирования, удаления категорий и подкатегорий товаров в админке.
3. [x] Категории и подкатегории обязательно должны иметь наименование, slug-имя, изображение
4. [x] Подкатегории должны быть связаны с родительской категорией
5. [x] Должен быть реализован эндпоинт для просмотра всех категорий с подкатегориями. Должны быть предусмотрена пагинация.
6. [x] Должна быть реализована возможность добавления, изменения, удаления продуктов в админке.
7. [x] Продукты должны относится к определенной подкатегории и, соответственно категории, должны иметь наименование, slug-имя, изображение в 3-х размерах, цену
8. [x] Должен быть реализован эндпоинт вывода продуктов с пагинацией. Каждый продукт в выводе должен иметь поля: наименование, slug, категория, подкатегория, цена, список изображений
9. [x] Реализовать эндпоинт добавления, изменения (изменение количества), удаления продукта в корзине.
10. [x] Реализовать эндпоинт вывода  состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
11. [x] Реализовать возможность полной очистки корзины
12. [x] Операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь
13. [x] Операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной
14. [x] Реализовать авторизацию по токену


### **Документация к API**


```
http://127.0.0.1:8000/api/users/

http://127.0.0.1:8000/api/token/login/

http://127.0.0.1:8000/api/categories/

http://127.0.0.1:8000/api/subcategories/

http://127.0.0.1:8000/api/products/

http://127.0.0.1:8000/api/products/{pk}/shopping_list/

http://127.0.0.1:8000/api/products/clear_shopping_list/

http://127.0.0.1:8000/api/shoppinglist/
```