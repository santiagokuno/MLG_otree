# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random
import ranking
import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Santiago GC'

doc = """
This and standard CPR game, but telling player groups their rankings
"""


class Constants(BaseConstants):
    name_in_url = 'CPR_Game_5'
    players_per_group = 4
    num_rounds = 1

    endowment = c(5)
    beta_factor = 0.35

class Subsession(BaseSubsession):

    rank_uno = models.DecimalField(max_digits=2, decimal_places=0)
    rank_dos = models.DecimalField(max_digits=2, decimal_places=0)
    rank_tres = models.DecimalField(max_digits=2, decimal_places=0)
    rank_cuatro = models.DecimalField(max_digits=2, decimal_places=0)
    rank_cinco = models.DecimalField(max_digits=2, decimal_places=0)

    rank_p_1 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_2 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_3 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_4 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_5 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_6 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_7 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_8 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_9 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_10 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_11 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_12 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_13 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_14 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_15 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_16 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_17 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_18 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_19 = models.DecimalField(max_digits=2, decimal_places=0)
    rank_p_20 = models.DecimalField(max_digits=2, decimal_places=0)

    posit_1 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_2 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_3 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_4 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_5 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_6 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_7 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_8 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_9 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_10 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_11 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_12 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_13 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_14 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_15 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_16 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_17 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_18 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_19 = models.DecimalField(max_digits=4, decimal_places=1)
    posit_20 = models.DecimalField(max_digits=4, decimal_places=1)

    max_pay = models.DecimalField(max_digits=3, decimal_places=1)
    min_pay = models.DecimalField(max_digits=3, decimal_places=1)

    max_fund = models.DecimalField(max_digits=3, decimal_places=1)
    min_fund = models.DecimalField(max_digits=3, decimal_places=1)

    def before_session_starts(self):
        if self.round_number == 1:
            players = self.get_players()
            random.shuffle(players)

            group_matrix = []

            ppg = Constants.players_per_group
            for i in range(0, len(players), ppg):
                group_matrix.append(players[i:i+ppg])
            self.set_groups(group_matrix)

        if self.round_number > 1:
            self.group_like_round(1)

    def set_ranking_g(self):
        self.max_fund = max([(Constants.endowment*Constants.players_per_group-p.total_extraction) for p in self.get_groups()])
        self.min_fund = min([(Constants.endowment*Constants.players_per_group-p.total_extraction) for p in self.get_groups()])
        vector_group = [(50-p.total_payment) for p in self.get_groups()]
        zeq = sorted (vector_group)
        indez = [zeq.index(v) for v in vector_group]
        vector_indez = [w + 1 for w in indez]
        self.rank_uno = vector_indez[0]
        self.rank_dos = vector_indez[1]
        self.rank_tres = vector_indez[2]
        self.rank_cuatro = vector_indez[3]
        self.rank_cinco = vector_indez[4]


    def set_ranking_p(self):
        self.max_pay = max([p.payoff for p in self.get_players()])
        self.min_pay = min([p.payoff for p in self.get_players()])
        vector_players = [(30-p.payoff) for p in self.get_players()]
        vector_positions = [p.participant_id for p in self.get_players()]
        seq = sorted(vector_players)
        index = [seq.index(v) for v in vector_players]
        vector_ranked_p = [w + 1 for w in index]
        self.rank_p_1 = vector_ranked_p[0]
        self.rank_p_2 = vector_ranked_p[1]
        self.rank_p_3 = vector_ranked_p[2]
        self.rank_p_4 = vector_ranked_p[3]
        self.rank_p_5 = vector_ranked_p[4]
        self.rank_p_6 = vector_ranked_p[5]
        self.rank_p_7 = vector_ranked_p[6]
        self.rank_p_8 = vector_ranked_p[7]
        self.rank_p_9 = vector_ranked_p[8]
        self.rank_p_10 = vector_ranked_p[9]
        self.rank_p_11 = vector_ranked_p[10]
        self.rank_p_12 = vector_ranked_p[11]
        self.rank_p_13 = vector_ranked_p[12]
        self.rank_p_14 = vector_ranked_p[13]
        self.rank_p_15 = vector_ranked_p[14]
        self.rank_p_16 = vector_ranked_p[15]
        self.rank_p_17 = vector_ranked_p[16]
        self.rank_p_18 = vector_ranked_p[17]
        self.rank_p_19 = vector_ranked_p[18]
        self.rank_p_20 = vector_ranked_p[19]
        self.posit_1 = vector_positions[0]
        self.posit_2 = vector_positions[1]
        self.posit_3 = vector_positions[2]
        self.posit_4 = vector_positions[3]
        self.posit_5 = vector_positions[4]
        self.posit_6 = vector_positions[5]
        self.posit_7 = vector_positions[6]
        self.posit_8 = vector_positions[7]
        self.posit_9 = vector_positions[8]
        self.posit_10 = vector_positions[9]
        self.posit_11 = vector_positions[10]
        self.posit_12 = vector_positions[11]
        self.posit_13 = vector_positions[12]
        self.posit_14 = vector_positions[13]
        self.posit_15 = vector_positions[14]
        self.posit_16 = vector_positions[15]
        self.posit_17 = vector_positions[16]
        self.posit_18 = vector_positions[17]
        self.posit_19 = vector_positions[18]
        self.posit_20 = vector_positions[19]


class Group(BaseGroup):

    total_extraction = models.DecimalField(max_digits=2, decimal_places=0)

    total_payment = models.CurrencyField()

    group_loss = models.CurrencyField()

    g_ranking = models.DecimalField(max_digits=2, decimal_places=0)

    def set_payoffs(self):
        self.total_extraction = sum([p.extraction for p in self.get_players()])
        self.group_loss = Constants.beta_factor * (Constants.players_per_group * Constants.endowment - self.total_extraction)
        for p in self.get_players():
            p.payoff = p.extraction + self.group_loss
        self.total_payment = sum([p.payoff for p in self.get_players()])

    def overall_payoffs(self):
        if self.id_in_subsession == 1:
            self.g_ranking = self.subsession.rank_uno
        elif self.id_in_subsession == 2:
            self.g_ranking = self.subsession.rank_dos
        elif self.id_in_subsession == 3:
            self.g_ranking = self.subsession.rank_tres
        elif self.id_in_subsession == 4:
            self.g_ranking = self.subsession.rank_cuatro
        elif self.id_in_subsession == 5:
            self.g_ranking = self.subsession.rank_cinco


class Player(BasePlayer):

    extraction = models.DecimalField(max_digits=2, decimal_places=0,
        min=0, max=Constants.endowment,
        choices=[0,1,2,3,4,5],
        doc="""The amount extracted by the player""",
    )

    ranking = models.DecimalField(max_digits=2, decimal_places=0)

    auxiliar = models.PositiveIntegerField()

    def the_ranking(self):
        self.auxiliar = self.participant_id
        if self.auxiliar == self.subsession.posit_1:
            self.ranking = self.subsession.rank_p_1
        elif self.auxiliar == self.subsession.posit_2:
            self.ranking = self.subsession.rank_p_2
        elif self.auxiliar == self.subsession.posit_3:
            self.ranking = self.subsession.rank_p_3
        elif self.auxiliar == self.subsession.posit_4:
            self.ranking = self.subsession.rank_p_4
        elif self.auxiliar == self.subsession.posit_5:
            self.ranking = self.subsession.rank_p_5
        elif self.auxiliar == self.subsession.posit_6:
            self.ranking = self.subsession.rank_p_6
        elif self.auxiliar == self.subsession.posit_7:
            self.ranking = self.subsession.rank_p_7
        elif self.auxiliar == self.subsession.posit_8:
            self.ranking = self.subsession.rank_p_8
        elif self.auxiliar == self.subsession.posit_9:
            self.ranking = self.subsession.rank_p_9
        elif self.auxiliar == self.subsession.posit_10:
            self.ranking = self.subsession.rank_p_10
        elif self.auxiliar == self.subsession.posit_11:
            self.ranking = self.subsession.rank_p_11
        elif self.auxiliar == self.subsession.posit_12:
            self.ranking = self.subsession.rank_p_12
        elif self.auxiliar == self.subsession.posit_13:
            self.ranking = self.subsession.rank_p_13
        elif self.auxiliar == self.subsession.posit_14:
            self.ranking = self.subsession.rank_p_14
        elif self.auxiliar == self.subsession.posit_15:
            self.ranking = self.subsession.rank_p_15
        elif self.auxiliar == self.subsession.posit_16:
            self.ranking = self.subsession.rank_p_16
        elif self.auxiliar == self.subsession.posit_17:
            self.ranking = self.subsession.rank_p_17
        elif self.auxiliar == self.subsession.posit_18:
            self.ranking = self.subsession.rank_p_18
        elif self.auxiliar == self.subsession.posit_19:
            self.ranking = self.subsession.rank_p_19
        elif self.auxiliar == self.subsession.posit_20:
            self.ranking = self.subsession.rank_p_20



