import requests

from core.celery_app import app


@app.task(bind=True)
def send_create_request(self, data, ip):
    print(ip + '/orders/')
    print(data)
    response = requests.post(ip + '/orders/', data=data)
    if response.status_code == 200:
        return
    else:
        self.retry(countdown=10, max_retries=0)


@app.task(bind=True)
def send_update_request(self, data, id, ip):
    print(ip + '/orders/')
    print(data)
    response = requests.put(f'{ip}/orders/{id}/', data=data)
    if response.status_code == 200:
        return
    else:
        self.retry(countdown=10, max_retries=0)
