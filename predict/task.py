from predict.celery import app
from task import task_post


@app.task(bind=True, max_retries=0)
def predict_image(self, key):
    print(key)