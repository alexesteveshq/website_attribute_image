# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Product Attribute Image',
    'summary': 'Adding images to attribute values. (website attribute image)',
    'description': 'Adding images to attribute values',
    'version': '17.0.1.0',
    'category': 'Website',
    'author': 'Visionee',
    'license': 'OPL-1',
    'depends': [
        'website_sale', 'stock',
    ],
    'data': [
        'templates/shop_product.xml',
        'views/product_attribute_value_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_attribute_image/static/src/**/*',
        ],
    },
    'images': [
        'static/description/banner.gif',
    ],
    'price': '30',
    'currency': "EUR",
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
