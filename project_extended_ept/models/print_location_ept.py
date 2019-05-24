"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class PrintLocation(models.Model):
    _name = "print.location.ept"

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    size = fields.Char(string='Size')
    
