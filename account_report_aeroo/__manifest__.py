{
    'name': 'Account (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Invoice report''',
    'depends': [
        'dec_report_aeroo',
        'company_fax',
        'account',
        'account_workflow_dec',
    ],
    'data':
        [
            'report/account_invoice.xml',
        ],
    'installable': True
}
