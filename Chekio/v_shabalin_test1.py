from grail import step, BaseTest

__author__ = 'v_shabalin'


class InvitationPageOpens(BaseTest):
    def test_invitation_page_with_steps(self):
        self.insert_to_active_players_table()
        self.open_invitation_page()
        self.fill_credentials()
        self.click_enter()
        self.check_text_invitation_page()

    @step
    def insert_to_active_players_table(self):
        pass

    @step
    def open_invitation_page(self):
        pass

    @step
    def fill_credentials(self):
        pass

    @step
    def click_enter(self):
        pass

    @step
    def check_text_invitation_page(self):
        pass




