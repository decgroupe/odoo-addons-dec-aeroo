{
    'name': 'Software License Pass (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': "Software license pass report",
    'depends': [
        'software_license_pass',
        'dec_report_aeroo',
    ],
    'data':
        [
            'report/software_license_pass.xml',
            'data/mail_template.xml',
        ],
    'installable': True
}
