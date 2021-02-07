from celery import Celery

app = Celery(broker="amqp://guest:guest@localhost:5672//", include=["core.tasks"])


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
