import os
from celery import Celery
from dotenv import load_dotenv


load_dotenv()

app = Celery(
    'predict_image',
    broker='amqp://{0}:{1}@{2}/{3}'.format(os.environ.get('RABBITMQ_USER'), os.environ.get('RABBITMQ_PWD'),
                                           os.environ.get('RABBITMQ_HOST'),
                                           os.environ.get('RABBITMQ_VHOST_POST')),
    backend='rpc://',
    include=["predict.task"]
)