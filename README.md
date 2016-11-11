# Flask-Page

Flask 프로젝트 내에서 Jinja2 로 작성한 정적 템플릿 파일을 처리할 수 있는 route 를 제공하는 모듈입니다.

## 설치 

``` 
$ pip install git+https://github.com/yoophi/flask-page.git#egg=Flask-Page
```

## 사용방법 

```python
from flask import Flask
from flask_page import init_app

app = Flask(__name__)
init_app(app)  # 또는 init_app(app, url_prefix='/p')

@route('/')
def index():
    return 'index'
```

프로젝트의 `templates/pages/index.html`, `templages/pages/sample/page1.html` 파일을 작성하면 
`http://locahost:5000/page/`, `http://localhost:5000/page/sample/page1` URL 로 접근 가능합니다.

