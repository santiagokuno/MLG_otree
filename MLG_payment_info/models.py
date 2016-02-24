# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'MLG_payment_info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def before_session_starts(self):
        for p in self.get_players():
            p.payoff = 0

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass