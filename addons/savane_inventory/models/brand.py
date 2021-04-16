from odoo import models, fields


class Brand(models.Model):
    _name = 'savane.brand'
    _description = 'Marque'

    name = fields.Char(string="Nom de la marque", required=True)
    description = fields.Text(string="Description de la marque")
