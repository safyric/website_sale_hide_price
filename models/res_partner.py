# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    website_show_price = fields.Boolean(string='Show prices on website', default=False,)
