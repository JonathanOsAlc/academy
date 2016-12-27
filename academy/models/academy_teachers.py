# -*- coding: utf-8 -*-
from odoo import models, api, fields

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()

class Course(models.Model):
	_name = 'academy.course'

	name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")
