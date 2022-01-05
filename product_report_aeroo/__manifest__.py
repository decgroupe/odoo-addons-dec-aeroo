{
    'name': 'Product (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Sale order report''',
    'depends': [
        'company_fax',
        'product',
        'product_seller',
        'dec_report_aeroo',
    ],
    'data':
        [
            'report/product_product_label.xml',
            'report/product_template_label.xml',
        ],
    'installable': True
}
