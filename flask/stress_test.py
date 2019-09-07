from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    
    @task(1)
    def index(self):
        self.client.get('/')
    
    @task(2)
    def elon_profile(self):
        self.client.get('/profile/elonmusk')
    
    @task(1)
    def mitsuhiko_profile(self):
        self.client.get('/profile/mitsuhiko')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000