from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    # res.user is a built-in model
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='Responsible', index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string='Sessions')
