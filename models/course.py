from odoo import fields, models


class Course(models.Model):
    _name = 'openacademy.course'

    title = fields.Char(string="Title")
    description = fields.Text(string="Description")
