{
    'name': 'Account Payment (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Voucher report''',
    'depends': [
        'dec_report_aeroo',
        'account',
    ],
    'data':
        [
            'report/account_payment.xml',
        ],
    'installable': True
}
