"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class InkColor(models.Model):
    _name = "ink.color.ept"
    _rec_name = "ink_color"

    ink_color = fields.Char(string='Ink Color')
    
