from grail import step, BaseTest
from spa.account import Account
from spa.steps.spa_http import SPAHttpApiSteps

__author__ = 'v_shabalin'

class BasicSmokeTest(BaseTest):
    spa_http_api_steps = SPAHttpApiSteps()

    @step
    def add_active_player(self):
        active_player = Account().generate()
        active_player.spa_id = self.spa_http_api_steps.create_registered_in_wot_account(account=active_player)
        return active_player