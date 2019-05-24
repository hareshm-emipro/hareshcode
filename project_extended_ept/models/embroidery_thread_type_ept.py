"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class EmibroideryThreadTypeEpt(models.Model):
    _name = "embroidery.thread.type.ept"
    _rec_name = "thread_type"

    thread_type = fields.Char(string='Thread_type')
    
