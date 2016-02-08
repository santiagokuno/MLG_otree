# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random
import ranking # introducido en 01/02/2016
import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Santiago GC'

doc = """
This is a common pool resource game with group competition
"""


class Constants(BaseConstants):
    name_in_url = 'MLG_Game'
    players_per_group = 2
    num_rounds = 1

    endowment = c(8)
    beta_factor = 0.6

class Subsession(BaseSubsession):

    multi_uno = models.DecimalField(max_digits=2, decimal_places=1)
    multi_dos = models.DecimalField(max_digits=2, decimal_places=1)

    def set_ranking(self):
        vector_group = [p.total_extraction for p in self.get_groups()]
        vector_ranked = ranking.rankdata(vector_group)
        coefficients = [2.5 - (a-1)*(2.0) for a in vector_ranked]
        self.multi_uno = coefficients[0]
        self.multi_dos = coefficients[1]

class Group(BaseGroup):

    total_extraction = models.DecimalField(max_digits=3, decimal_places=1)

    group_loss = models.DecimalField(max_digits=3, decimal_places=1)

    def set_payoffs(self):
        self.total_extraction = sum([p.extraction for p in self.get_players()])
        self.group_loss = Constants.beta_factor * (Constants.players_per_group * Constants.endowment - self.total_extraction)
        for p in self.get_players():
            p.payoff = p.extraction + self.group_loss

    def overall_payoffs(self):
        if self.id_in_subsession == 1:
            for p in self.get_players():
                p.payoff = p.payoff*self.subsession.multi_uno
        elif self.id_in_subsession == 2:
            for p in self.get_players():
                p.payoff = p.payoff*self.subsession.multi_dos


class Player(BasePlayer):

    extraction = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""The amount extracted by the player""",
    )

