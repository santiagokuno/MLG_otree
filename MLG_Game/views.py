# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Contribute(Page):

    """Player: Choose how much to extract"""

    form_model = models.Player
    form_fields = ['extraction']

    timeout_submission = {'extraction': c(Constants.endowment/2)}

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Calculating payoffs by group."

class Results(Page):
    pass
    """Players payoff: How much each has earned"""

class AnotherWaitPage(WaitPage):

    wait_for_all_groups = True

    body_text = "Waiting for other participants to advance."

class Results_2WaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.subsession.set_ranking()

    body_text = "Calculating payoffs by group."

class Results_3WaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.overall_payoffs()

    body_text = "This is another one."

class Results_2(Page):
    #pass
    def vars_for_template(self):
        return {
            'multiplicador_uno': self.subsession.multi_uno,
            'multiplicador_dos': self.subsession.multi_dos,
        }


page_sequence = [
    Contribute,
    ResultsWaitPage,
    Results,
    AnotherWaitPage,
    Results_2WaitPage,
    Results_3WaitPage,
    Results_2
]
