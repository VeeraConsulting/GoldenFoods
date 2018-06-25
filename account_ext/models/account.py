# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp

class InvoiceOrderLine(models.Model):
    _inherit = "account.invoice.line"

    margin = fields.Float(compute='_product_margin', digits=dp.get_precision('Product Price'), store=True)

    @api.depends('product_id','quantity')
    def _product_margin(self):
        """
         Count the margin per product inside invoice line.
        :return: margin of each product.
        """
        for invoice_line in self:
            if invoice_line.invoice_id and invoice_line.invoice_id.origin and \
                invoice_line.invoice_id.origin.startswith('SO'):
                sale_order = self.env['sale.order'].search([('name','=',invoice_line.invoice_id.origin)],limit=1)
                if sale_order and sale_order.order_line:
                    for order_line in sale_order.order_line:
                        if order_line.product_id == invoice_line.product_id:
                            per_qty_margin = order_line.margin / order_line.product_uom_qty
                            invoice_line.margin = per_qty_margin * invoice_line.quantity


class InvoiceOrder(models.Model):
    _inherit = "account.invoice"

    margin = fields.Float(compute='_total_margin', digits=dp.get_precision('Margin'), store=True)

    @api.depends('invoice_line_ids')
    def _total_margin(self):
        """
        Count the total margin of invoice.
        :return: margin of invoice.
        """
        for invoice in self:
            margin = 0
            if invoice.invoice_line_ids:
                for invoice_line in invoice.invoice_line_ids:
                    if invoice_line.margin:
                        margin += invoice_line.margin
            invoice.margin = margin
