# -*- coding: utf-8 -*-
{
    'name': "Savane Inventory Delivery Slip Extension",

    'summary': """
        This module extends the delivery slip form and report.
        """,

    'description': """
        This module extends the delivery slip form and report. New fields "Color" and "Brand" are required in 
        the form then filled in by the user. They are displayed in the delivery slip report.
    """,

    'author': "Savane Industrie",
    'website': "http://www.erp-savane.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/savane.xml',
        'views/stock_move.xml',
        'reports/report_stockpicking_operations.xml',
        'reports/report_deliveryslip.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}