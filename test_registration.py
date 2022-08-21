import pytest

import home_page
from home_page import Homepage
from dotenv import load_dotenv
import os

load_dotenv()


class Test:
    @staticmethod
    @pytest.mark.parametrize("user_data",
                             [([os.getenv('FIRST_NAME'), (os.getenv('LAST_NAME')), os.getenv('LOGIN1'),
                               os.getenv('PSWD1')]),
                              ([os.getenv('FIRST_NAME'), (os.getenv('LAST_NAME')), os.getenv('LOGIN2'),
                               os.getenv('PSWD2')])])
    def test_reg(user_data):
        Homepage = home_page.Homepage()
        Homepage.enter_name(user_data[0], user_data[1])
        Homepage.enter_email(user_data[2])
        Homepage.enter_pswd(user_data[3])
        Homepage.submit('registration')


    @staticmethod
    @pytest.mark.parametrize("user_data",
                             [([os.getenv('LOGIN1'), os.getenv('PSWD1')]),
                              ([os.getenv('LOGIN2'), os.getenv('PSWD2')])])
    def test_check_login(user_data):
        Homepage = home_page.Homepage()
        Homepage.switch_to_sign_in()
        Homepage.enter_email(user_data[0])
        Homepage.enter_pswd(user_data[1])
        Homepage.submit('login')


