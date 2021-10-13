{
    'name': 'Overdue Invoice Reminder (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "Simple mail/letter/phone overdue customer invoice reminder",
    'depends': [
        'dec_report_aeroo',
        'account_invoice_overdue_reminder',
    ],
    'data': ['report/overdue_reminder.xml', ],
    'installable': True
}
