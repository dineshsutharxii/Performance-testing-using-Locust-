from locust import HttpUser, task, between


class Locustdayone(HttpUser):
    wait_time = between(1, 2)

    @task
    def test(self):
        post_load = {
            "email": "jogidemo321@gmail.com",
            "password": "builder123"
        }
        login_api = '/users/sign_in'
        response = self.client.post(url=login_api, json=post_load)
        json_data = response.json()
        auth_token = json_data['user']['authtoken']
        print(auth_token)
