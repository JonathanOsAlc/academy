# -*- coding: utf-8 -*-
{
    'name': "Academy",

    'summary': """
        Building a Website""",

    'description': """
        Academy module for managing trainings:
            - For buid a website
    """,

    'author': "Vauxoo",
    'website': "http://www.vaouxoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'mail',
        'website_sale',
        ],

    # always loaded
    'data': [
         #'security/ir.model.access.csv',
         'views/academy_views.xml',
         'views/academy_templates.xml',
         'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/academy_demo.xml',
    ],
}