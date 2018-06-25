# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError
import datetime

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _compute_total_ordered_qty(self):
        """
        Calculate total ordered qty of order.
        :return: total ordered qty of order.
        """
        for sale_order in self:
            qty = 0
            for order_line in sale_order.order_line:
                if order_line.product_uom_qty:
                    qty+= order_line.product_uom_qty
            sale_order.total_ordered_qty = qty

    total_ordered_qty = fields.Float('Ordered Qty', compute='_compute_total_ordered_qty')

    @api.model
    def create(self,vals):
        res = super(SaleOrder, self).create(vals)
        if vals.get("partner_id"):
            invoices = self.env['account.invoice'].search([('state','=','open'),
                                                           ('partner_id','=',vals.get('partner_id'))])
            # Generate the warning if Partners's invoice exceeded from 60 days and can not create sale order
            for invoice in invoices:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                date_diff = datetime.datetime.strptime(current_date, "%Y-%m-%d") \
                            - datetime.datetime.strptime(invoice.date_invoice, "%Y-%m-%d")
                if date_diff.days > 60:
                    raise UserError(_("The following customer has invoices outstanding more than 60 days - please \
                                request customer to clear all balances over 60 days in order to generate new orders."))

                # Generate the warning when credit limit is over and can not create sale order
            outstanding_balance =  res.partner_id.credit_limit - res.partner_id.credit
            if res.amount_total > outstanding_balance:
                raise UserError(_("The sales order amount exceeds the customer's remaining credit limit - please \
                                  request customer to pay older invoices or ensure new sales order does not exceed  \
                                  available limit."))
        return res



