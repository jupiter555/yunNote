# yunNote
practice of using cookies&amp;session about django

- 1. 创建数据库　命名为mysite6
- 2. 迁移,同步数据库,在根目录(包含manage.py)的文件夹下执行
```mysql
python3 manage.py makemigrations,
python3 manage.py migrate
```
- 3. 运行服务端
```python
python3 manage.py runserver
```
- 4. 打开网页
```html
登录页面：http://127.0.0.1:8000/user/login
注册页面：http://127.0.0.1:8000/user/reg
笔记列表页面：http://127.0.0.1:8000/note/
添加笔记页面：http://127.0.0.1:8000/note/add
```
