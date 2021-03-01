from odoo import models, fields


class Partner(models.Model):
    """This class inherit the built-in odoo partner"""
    _inherit = 'res.partner'
    # Add a new column to the res.partner model, by default partners are not instructors
    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)
