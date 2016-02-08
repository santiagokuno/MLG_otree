# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Intro_I(Page):
    pass

class Intro_II(Page):
    pass

page_sequence = [
    Intro_I,
    Intro_II
]
