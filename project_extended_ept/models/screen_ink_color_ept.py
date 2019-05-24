"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _

class ScreenInkColorEpt(models.Model):
    _name = "screen.ink.color.ept"
    _rec_name = "ink_color"

    
    ink_color = fields.Char(string='Ink Color')
    screen_ink_type_id = fields.Many2one('screen.ink.type.ept', string=_('Screen Ink type'))
    
    
    
    
    
    
