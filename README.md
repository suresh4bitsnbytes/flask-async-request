# flask-async-request

Python Flask asynchronous request response pattern using celery.
  
## Prerequisite
- [python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [redis](https://redis.io/docs/getting-started/installation/)

## Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules.

```bash

python -m venv .venv

source .venv/bin/activate (unix)

pip install -r requirements.txt

```
### Redis server
```bash
 redis-server
```
### Celery worker
```bash
celery -A app.celery worker --loglevel=INFO
```

### Start flask dev server
```bash
export FLASK_APP="app"

export FLASK_ENV="development"

flask run
```
