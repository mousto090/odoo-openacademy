from odoo import models, fields


class Color(models.Model):
    _name = 'savane.color'
    _description = 'Couleur'

    name = fields.Char(string="Nom de la couleur", required=True)
    code = fields.Char(string="Code de la couleur")
