# -*- coding: utf-8 -*-

from odoo import models, fields


class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()

    course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")


class Courses(models.Model):
    _name = 'academy.courses'
    # _inherit = ['mail.thread', 'product.template']
    _inherit = 'mail.thread'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")
