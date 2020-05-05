{
    'name': 'Purchase (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Purchase order report''',
    'depends': [
        'company_fax',
        'purchase',
        'product_pack',
    ],
    'data':
        [
            'report/purchase_order.xml',
            'wizard/purchase_custom_report.xml',
        ],
    'installable': True
}
