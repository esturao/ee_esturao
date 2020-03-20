# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    hide_margin =fields.Boolean("Hide margin", default=True, help='Hide or show sales margin as needed.')
    
    @api.onchange('hide_margin') # if these fields are changed, call method
    def check_change(self):
        for line in self.order_line:
            line.hide_margin = self.hide_margin
    
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    hide_margin =fields.Boolean("Hide margin", default=True, help='Hide or show sales margin as needed.')
