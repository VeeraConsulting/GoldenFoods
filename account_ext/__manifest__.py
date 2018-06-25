# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Account Extension",
    "version": "1.0",
    "author": "Anil R. Kesariya",
    "category": "Accounting",
    "summary": "",
    "depends": [
        'sale_margin','account_invoicing'
    ],
    'description': """

Account Enhancement
===================

Added margin inside invoice, Calculated it based on the associated sale order's cost price.

        """,
    "demo": [],
    "data": [
        'views/account_view.xml',
    ],
    "installable": True,
    "auto_install": False,
}
