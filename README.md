# Setting Up a Python Environment and Running a Flask Application

## 1. Create Python Environment

```bash
apt install python3.12-venv

python3 -m venv myenv
source myenv/bin/activate
```

## 2. Install Flask

```bash
pip install flask
pip list
```

## 3. Create `app.py` File

Create a file named `app.py` with the following content:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
```

## 4. Run the Web Server

```bash
python3 app.py
```

## 5. Exit the Virtual Environment

```bash
deactivate
```
