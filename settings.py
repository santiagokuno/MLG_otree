import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'otree'

# don't share this with anybody.
# Change this to something unique (e.g. mash your keyboard),
# and then delete this comment.
SECRET_KEY = 'zzzzzzzzzzzzzzzzzzzzzzzzzzz'

PAGE_FOOTER = ''

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# ACCESS_CODE_FOR_DEFAULT_SESSION:
# If you have a "default session" set,
# then an access code will be appended to the URL for authentication.
# You can change this as frequently as you'd like,
# to prevent unauthorized server access.

ACCESS_CODE_FOR_DEFAULT_SESSION = 'my_access_code'

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COL'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 1
# "USD"

# e.g. en-gb, de-de, it-it, fr-fr.
# see: https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'es'
# 'en-us'


# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = []

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            Source code
        </a> for the below games.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Below are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish to create your own variations.
    Click one to learn more and play.
</p>
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        qualification.LocaleRequirement("EqualTo", "US"),
        qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        #qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 500,
    'participation_fee': 5000,
    'num_bots': 12,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
#    {
#        'name': 'public_goods',
#        'display_name': "Public Goods",
#        'num_demo_participants': 3,
#        'app_sequence': ['public_goods', 'payment_info'],
#    },
#    {
#        'name': 'public_goods_simple',
#        'display_name': "Public Goods (simple version from tutorial)",
#        'num_demo_participants': 3,
#        'app_sequence': ['public_goods_simple', 'survey', 'payment_info'],
#    },
#    {
#        'name': 'trust',
#        'display_name': "Trust Game",
#        'num_demo_participants': 4,
#        'app_sequence': ['trust', 'payment_info'],
#    },
#    {
#        'name': 'trust_simple',
#        'display_name': "Trust Game (simple version from tutorial)",
#        'num_demo_participants': 2,
#        'app_sequence': ['trust_simple'],
#    },
#    {
#        'name': 'beauty',
#        'display_name': "Beauty Contest",
#        'num_demo_participants': 5,
#        'num_bots': 5,
#        'app_sequence': ['beauty', 'payment_info'],
#    },
#    {
#        'name': 'survey',
#        'display_name': "Survey",
#        'num_demo_participants': 1,
#        'app_sequence': ['survey', 'payment_info'],
#    },
#    {
#        'name': 'prisoner',
#        'display_name': "Prisoner's Dilemma",
#        'num_demo_participants': 2,
#        'app_sequence': ['prisoner', 'payment_info'],
#    },
#    {
#        'name': 'ultimatum',
#        'display_name': "Ultimatum (randomized: strategy vs. direct response)",
#        'num_demo_participants': 2,
#        'app_sequence': ['ultimatum', 'payment_info'],
#    },
#    {
#        'name': 'ultimatum_strategy',
#        'display_name': "Ultimatum (strategy method treatment)",
#        'num_demo_participants': 2,
#        'app_sequence': ['ultimatum', 'payment_info'],
#        'treatment': 'strategy',
#    },
#    {
#        'name': 'ultimatum_non_strategy',
#        'display_name': "Ultimatum (direct response treatment)",
#        'num_demo_participants': 2,
#        'app_sequence': ['ultimatum', 'payment_info'],
#        'treatment': 'direct_response',
#    },
#    {
#        'name': 'battle_of_the_sexes',
#        'display_name': "Battle of the Sexes",
#        'num_demo_participants': 2,
#        'app_sequence': [
#            'battle_of_the_sexes', 'payment_info'
#        ],
#    },
#    {
#        'name': 'vickrey_auction',
#        'display_name': "Vickrey Auction",
#        'num_demo_participants': 3,
#        'app_sequence': ['vickrey_auction', 'payment_info'],
#    },
#    {
#        'name': 'volunteer_dilemma',
#        'display_name': "Volunteer's Dilemma",
#        'num_demo_participants': 3,
#        'app_sequence': ['volunteer_dilemma', 'payment_info'],
#    },
#    {
#        'name': 'cournot_competition',
#        'display_name': "Cournot Competition",
#        'num_demo_participants': 2,
#        'app_sequence': [
#            'cournot_competition', 'payment_info'
#        ],
#    },
#    {
#        'name': 'principal_agent',
#        'display_name': "Principal Agent",
#        'num_demo_participants': 2,
#        'app_sequence': ['principal_agent', 'payment_info'],
#    },
#    {
#        'name': 'dictator',
#        'display_name': "Dictator Game",
#        'num_demo_participants': 2,
#        'app_sequence': ['dictator', 'payment_info'],
#    },
#    {
#        'name': 'matching_pennies',
#        'display_name': "Matching Pennies",
#        'num_demo_participants': 2,
#        'app_sequence': [
#            'matching_pennies', 'payment_info'
#        ],
#    },
#    {
#        'name': 'matching_pennies_tutorial',
#        'display_name': "Matching Pennies (tutorial version)",
#        'num_demo_participants': 2,
#        'app_sequence': [
#            'matching_pennies_tutorial',
#        ],
#    },
#    {
#        'name': 'traveler_dilemma',
#        'display_name': "Traveler's Dilemma",
#        'num_demo_participants': 2,
#        'app_sequence': ['traveler_dilemma', 'payment_info'],
#    },
#    {
#        'name': 'bargaining',
#        'display_name': "Bargaining Game",
#        'num_demo_participants': 2,
#        'app_sequence': ['bargaining', 'payment_info'],
#    },
#    {
#        'name': 'common_value_auction',
#        'display_name': "Common Value Auction",
#        'num_demo_participants': 3,
#        'app_sequence': ['common_value_auction', 'payment_info'],
#    },
#    {
#        'name': 'stackelberg_competition',
#        'display_name': "Stackelberg Competition",
#        'real_world_currency_per_point': 0.01,
#        'num_demo_participants': 2,
#        'app_sequence': [
#            'stackelberg_competition', 'payment_info'
#        ],
#    },
#    {
#        'name': 'bertrand_competition',
#        'display_name': "Bertrand Competition",
#        'num_demo_participants': 2,
#        'app_sequence': [
#            'bertrand_competition', 'payment_info'
#        ],
#    },
#    {
#        'name': 'stag_hunt',
#        'display_name': "Stag Hunt",
#        'num_demo_participants': 2,
#        'app_sequence': ['stag_hunt', 'payment_info'],
#    },
#    {
#        'name': 'real_effort',
#        'display_name': "Real-effort transcription task",
#        'num_demo_participants': 1,
#        'app_sequence': [
#            'real_effort',
#        ],
#    },
#    {
#        'name': 'lemon_market',
#        'display_name': "Lemon Market Game",
#        'num_demo_participants': 3,
#        'app_sequence': [
#            'lemon_market', 'payment_info'
#        ],
#    },
        {
        'name': 'Instrucciones',
        'display_name': "Instrucciones",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Intro'
        ],
    },
       {
        'name': 'Primera_Etapa',
        'display_name': "Primera_etapa",
        'num_demo_participants': 12,
        'app_sequence': [
            'CPR_Game'
        ],
    },
        {
        'name': 'Cambio_Regla_I',
        'display_name': "Cambio_regla",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Change'
        ],
    },
        {
        'name': 'Segunda_Etapa',
        'display_name': "Segunda_etapa",
        'num_demo_participants': 12,
        'app_sequence': [
            'MLG_Game'
        ],
    },
       {
        'name': 'Encuesta',
        'display_name': "Encuesta",
        'num_demo_participants': 1,
        'app_sequence': [
             'MLG_survey'
        ],
    },
       {
        'name': 'Completo',
        'display_name': "MLG Full",
        'num_demo_participants': 12,
        'app_sequence': [
             'MLG_Intro', 'CPR_Game', 'MLG_Change', 'MLG_Game', 'MLG_survey'
        ],
    },
]

SENTRY_DSN = 'http://7b6ef95ec90b4cddaf09ca55184f6ef1:e5fd539d433949fab29a6acc04fab93a@sentry.otree.org/13'

otree.settings.augment_settings(globals())


