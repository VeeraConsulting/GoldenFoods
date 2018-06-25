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
	
     - Added Validation on credit limit and due date
     - Added Sub Total of Deliverd Qty, Ordered Qty and Invoiced Qty
     - Added two warrnings :
       1. 'User Error',Selected partner's past invoice due from 60 days cannot creat new order for the customer.
       2. 'User Error', Credit limit is left  %.2f only, cannot create order with %.2f amoun
 
        """,
    "demo": [],
    "data": [
        'views/sale_order.xml',
        'views/res_partner.xml',
    ],
    "installable": True,
    "auto_install": False,
}
