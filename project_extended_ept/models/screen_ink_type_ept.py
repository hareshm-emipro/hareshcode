"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _

class ScreenInkTypeEpt(models.Model):
    _name = "screen.ink.type.ept"
    _rec_name = "ink_type"

    ink_type = fields.Char(string='Ink Type')
    

    
