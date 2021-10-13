{
    'name': 'Production (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Production report''',
    'depends': [
        'company_fax',
        'product_location',
        'mrp',
        'mrp_traceability',
        'mrp_note',
        'mrp_workflow_dec',
        'mrp_picked_rate',
        'mrp_product_pack',
        'dec_report_aeroo',
    ],
    'data':
        [
            'report/mrp_production.xml',
            'wizard/mrp_production_custom_report.xml',
        ],
    'installable': True
}
