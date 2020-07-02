{
    'name': 'Production (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Production report''',
    'depends': [
        'company_fax',
        'mrp',
        'dec_report_aeroo',
    ],
    'data':
        [
            'report/mrp_production.xml',
            'wizard/mrp_production_custom_report.xml',
        ],
    'installable': True
}
