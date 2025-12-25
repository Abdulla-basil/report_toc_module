# -*- coding: utf-8 -*-
{
    'name': "Report Table of Contents (ToC)",
    'summary': "Generate automated Table of Contents for PDF reports to improve document navigation",
    'description': """
Table of Contents for Odoo Reports
==================================
This module allows users to automatically generate a Table of Contents (ToC) for complex PDF reports. 
It is designed to improve document navigation for long business records such as catalogs, 
lengthy quotations, or technical manuals.

**Key Features**
----------------
* Automatically generate a Table of Contents (ToC).
* Customise ToC styling via standard QWeb templates.
* Improve document navigation for long business records.
* Seamless integration with existing Odoo PDF reports.
* Lightweight and easy to configure.

**Use Case**
------------
Perfect for companies generating large reports where page numbers and section 
references are critical for professional presentation.

**Compatibility**
-----------------
Odoo 17.0 Community and Enterprise.
    """,

    'author': "Abdulla Basil",
    'website': "",
    'category': 'Reporting',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',

    # If this is a paid module, uncomment the two lines below:
    # 'price': 15.00,
    # 'currency': 'EUR',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_action.xml',
        'reports/report_template.xml',
    ],

    'images': [
        'static/description/banner.png',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}