from locust import HttpUser, TaskSet, task, between

class Locust_chaining(HttpUser):
    token = "unable to fetch"

    def get_token(self):
        login_api = '/users/sign_in'
        post_load = {
            "email": "jogidemo321@gmail.com",
            "password": "builder123"
        }
        login_api = '/users/sign_in'
        response = self.client.post(url=login_api, json=post_load)
        json_data = response.json()
        auth_token = json_data['user']['authtoken']
        print(auth_token)

    def on_start(self):
        self.client.headers['Contect-Type'] = "application/json"
        self.client.headers['authtoken'] = self.get_token()

    @task
    def test_dashboard_api(self):
        response = self.client.get("/build_cards?status=completed")
        card_count = response.json()['build_card_count']['completed']
        if card_count < 1:
            response.failure("dashboard api failed because completed count is less than 1")

    @task
    def test_config_api(self):
        response = self.client.get("/configurations")
        if response.json()['valid_user'] == "True":
            response.failure("Config api failed because user is not valid")

class E2EloadTest(HttpUser):
    wait_time = between(1, 2)
    tasks = [Locust_chaining]
    host = "https://api-staging-builder.engineer.ai"
