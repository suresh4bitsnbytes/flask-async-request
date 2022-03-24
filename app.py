import time

from flask import Flask
from tasks import make_celery

app = Flask(__name__) 
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)


@celery.task()
def add(a, b):
    time.sleep(5)
    return a + b


@app.route('/')
def add_two_nimbers():
    add.delay(23, 42)
    return 'async celery task initiated', 200
