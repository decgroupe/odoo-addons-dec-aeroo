{
    'name': 'Sale (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Sale order report''',
    'depends': [
        'company_fax',
        'sale',
        'sale_warranty',
        'product_pack',
        'sale_product_pack',
        'dec_report_aeroo',
    ],
    'data':
        [
            'report/sale_order.xml',
        ],
    'installable': True
}
