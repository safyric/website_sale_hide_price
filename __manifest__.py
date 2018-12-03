# -*- coding: utf-8 -*-
{
    'name': "Hide Website Sale Price",

    'summary': """Hide website sale price""",

    'description': """Hide website sale price""",

    'author': "Safyric Co., Ltd.",
    'website': "https://www.safyric.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/partner_view.xml',
        'views/website_sale_template.xml',
        'views/website_sale_wishlist',
    ],
    'installable': True,
}
