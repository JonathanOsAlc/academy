# -*- coding: utf-8 -*-
from odoo import models, api, fields

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()
