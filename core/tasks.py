from core.celery_app import app
from core.services.communication import CommunicationService


@app.task(bind=True)
def sync_order(self, base_url, data, order_id, method):
    try:
        CommunicationService(base_url).send_request(data, order_id, method)
    except Exception as e:
        print(e)
        self.retry(countdown=30, max_retries=3)
