"""
    Developed By: Haresh Mori
    Extended Project For project task creating while return picking create and validate.
"""

from odoo import fields, models, api, _
from odoo.exceptions import Warning


class ProjectTask(models.Model):
    """ Added two field in project task model """
    _inherit = "project.task"

    return_picking_id = fields.Many2one('stock.picking', string=_('Return Picking'))
    sale_order_id = fields.Many2one('sale.order', string=_('Sale Order'))
    #for SCREEN PRINTING project
    print_location_id  = fields.Many2one('print.location.ept', string=_('Print Locations'))
    garment_material_id  = fields.Many2one('garment.material.ept', string=_('Garment Material'))
    distress_level = fields.Selection([('DL0','No Distress'),('DL1','Distress Level 1'),('DL2','Distress Level 2'),('DL3','Distress Level 3'),('DL4','Distress Level 4'),('CD','Custom Distress')],string=_('Distress Level'))
    smallest_size = fields.Selection([('YSM','Youth Small'),('YMD','Youth Medium'),('YLG','Youth Large'),('YXL','Youth X Large'),('XSM','X Small'),('SML','Small'),
                                      ('MED','Medium'),('LRG','Large'),('XLG','X Large'),('XXL','XX Large'),('3XL','3X Large'),('4XL','4X Large')],string=_('Smallest Size'))
    garment_style = fields.Text('Garment Style')
    garment_shade = fields.Selection([('dark','Dark'),('light','Light'),('white','White')])
    decoration_color = fields.Text('Decoration Color')
    screen_mesh_size = fields.Selection([('86','86'),('110','110'),('156','156'),('200','200'),('230','230'),('305','305')],string=_('Screen Mesh Size'))
    Squeegee = fields.Selection([('50_durometer','Extremely Soft'),('60_durometer','Soft'),('70_durometer','Medium'),('80_durometer','Hard'),('90_durometer','Extremely Hard')],string=_('Squeegee'))
    projects = fields.Selection([('scr','[SCR]Screen Printing'),('vyn','[vyn]Vinyl'),('sub','[SUB]Sublimation'),('emb','[EMB]Embroidery'),('cht','[CHT]Wall Chart'),('hdg','[HDG]Heargear Wrap')])
    oven_temp = fields.Integer(string='Oven Temp')
    oven_speed = fields.Integer(string='Oven Speed')
    ink_type_ids = fields.One2many('screen.ink.color.type.ept','project_id',string="Screen Ink Type Color")
    
    #for Vinyl project
    material = fields.Selection([('tdb','TDB')],string=_('Material'))
    material_color = fields.Selection([('color','Color')],string=_('Material Color'))
    press_temp = fields.Integer(string='Press Temp')
    press_pressure = fields.Integer(string='Press Pressure')
    press_time = fields.Integer(string='Press Time(seconds)')
    vinyl_material_color_ids = fields.One2many('vinyl.material.color.ept','project_id',string="Vinyl Material Color")
    #for sublimation project
    sublimation_press_temp = fields.Integer(string='Press Temp')
    sublimation_press_pressure = fields.Integer(string='Press Pressure')
    sublimation_press_time = fields.Text(string='Press Time(seconds)')
    #for Embroidery project
    thread_type_color_ids = fields.One2many('embroidery.thread.type.color.ept','project_id',string="Embroidery Thread Type Color")
    #for WALL CHARTS project
    template_number = fields.Selection([('wc01','WC01'),('wc02','WC02'),('wc03','WC03'),('wc04','WC04'),('wc05','WC05')
                                        ,('wc06','WC06'),('wc07','WC07'),('wc08','WC08'),('wc09','WC09'),('wc10','WC10')
                                        ,('wc11','WC11'),('wc12','WC12'),('wc13','WC13'),('wc14','WC14'),('wc15','WC15')
                                        ,('wc16','WC16'),('wc17','WC017'),('wc18','WC18'),('wc19','WC19'),('wc20a','WC20A')
                                        ,('wc20b','WC20B')],string=_('Template Number'))
    wall_chart_paper_size = fields.Text(string='Paper Size')
    wall_chart_artwork_file = fields.Binary('Artwork File')
    wall_chart_sample_photo = fields.Binary('Sample Photo')
    #for Headgear Wrap project
    headgear_type = fields.Selection([('E58','Signature Headgear'),('E58W','Two-Tone Signature Headgear'),('AE100','Response Headgear'),('AE100B','Response Headgear w/Black Straps')])
    decoration_color = fields.Char(string='Decoration Color')

    
    
    
    
    @api.model
    def create(self,vals):
        res = super(ProjectTask,self).create(vals)
        default_assign_id = res.project_id.default_assigned_id
        if default_assign_id:
            res.write({'user_id':default_assign_id.id})
        else:
            raise Warning('There is no default assign in %s'%(res.project_id.name))
        if res.project_id.projects:
            res.write({'projects':res.project_id.projects}) 
        account_analytic_line_obj = self.env["account.analytic.line"]
        project_employee = res.project_id.timeshets_employee_ids
        if project_employee:
            for employee in project_employee:
                account_analytic_line_id = account_analytic_line_obj.create({'employee_id':employee.id,'unit_amount':0,'task_id':res.id,'account_id':res.project_id.analytic_account_id.id})
        return res
    
    
    
    
    @api.onchange('project_id')
    def _onchange_project(self):
        """
        @author: Haresh Mori on date 25/04/2019
        This method is override the base method of project_id on change.This method user for set projects in task. 
        """
        
        res = super(ProjectTask,self)._onchange_project()
        if self.project_id.projects:
            self.projects = self.project_id.projects
        return res

    
    
    

    
    

    
    


