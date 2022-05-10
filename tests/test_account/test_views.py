from test_account.test_setup import TestSetUp


class TestRegisterView(TestSetUp):
    def test_user_cannot_register(self):
        res = self.client.post(self.register_url)
        print(res)
        assert res.status_code == 400
