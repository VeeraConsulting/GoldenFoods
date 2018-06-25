{
    "name": "Sale Order Extension",
    "version": "1.0",
    "author": "Anil R. Kesariya",
    "category": "Sales",
    "summary": "",
    "depends": [
        'sale_management','account_invoicing', 'contacts', 'account_reports'
    ],
    'description': """

Sale Order Enhancement
======================

Added validation on credit limit and due date.

Added sub total of deliverd qty, ordered qty and invoiced qty.

Added two warnings :
    1. The following customer has invoices outstanding more than 60 days - please request customer to clear all balances
        over 60 days in order to generate new orders.
    2. The sales order amount exceeds the customer's remaining credit limit - please request customer to pay older invoices
        or ensure new sales order does not exceed available limit
 
        """,
    "demo": [],
    "data": [
        'views/sale_order.xml',
        'views/res_partner.xml',
    ],
    "installable": True,
    "auto_install": False,
}
