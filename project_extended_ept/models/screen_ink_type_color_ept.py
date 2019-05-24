"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _

class ScreenInkTypeColorEpt(models.Model):
    _name = "screen.ink.color.type.ept"


    screen_ink_color_id = fields.Many2one('screen.ink.color.ept', string=_('Screen Ink Color'))
    screen_ink_type_id = fields.Many2one('screen.ink.type.ept', string=_('Screen Ink Type'))
    project_id = fields.Many2one('project.task', string=_('Project Task'))
    
