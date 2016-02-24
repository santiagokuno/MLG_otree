# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Cambio(Page):
    pass

class Pregunta(Page):

    form_model = models.Player
    form_fields = ['question']

class Respuesta(Page):
    pass


page_sequence = [
    Cambio,
    Pregunta,
    Respuesta
]
