from odoo import models, api, fields, _
from odoo.exceptions import UserError
import datetime

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _compute_total_ordered_qty(self):
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
            invoices = self.env['account.invoice'].search([('state','=','open'),('partner_id','=',vals.get('partner_id'))])
            # Generate the warning if Partners's invoice exceeded from 60 days and can not create sale order
            for invoice in invoices:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                date_diff = datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.datetime.strptime(invoice.date_invoice, "%Y-%m-%d")
                if date_diff.days > 60:
                    raise UserError(_("'User Error',Selected partner's past invoice due from 60 days cannot creat new order for the customer."))

                # Generate the warning when credit limit is over and can not create sale order
            outstanding_balance =  res.partner_id.credit_limit - res.partner_id.credit
            if res.amount_total > outstanding_balance:
                raise UserError(_("'User Error', Credit limit is left  %.2f only, cannot create order with %.2f amount") % (outstanding_balance,res.amount_total))
        return res



