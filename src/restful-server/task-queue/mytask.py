import time
from celery import Celery

celery = Celery('tasks', 
                broker='redis://localhost:6379',
                backend='redis://localhost:6379')
 
@celery.task
def add(x, y):
    return x + y

@celery.task
def send_file(fname, file):
    print("Start to send the file...")
    time.sleep(10)
    print("Finished.")
    return True
 