# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Mar 2020

from odoo import _
from odoo.addons.report_aeroo.extra_functions import aeroo_util
from odoo.tools.misc import formatLang, format_date
from odoo.tools import html2plaintext
from types import SimpleNamespace


@aeroo_util('html2plaintext')
def _html2plaintext(report, html, body_id=None, encoding='utf-8'):
    return html2plaintext(html, body_id, encoding)


@aeroo_util('set')
def set(report, name, value):
    '''
    <set('partner', o.partner_id or (o.move_lines and o.move_lines[0].partner_id) or False)>
    <if test="t.partner">
    '''
    if not 't' in report.env.context:
        report.env.context['t'] = SimpleNamespace()
    setattr(report.env.context['t'], name, value)


@aeroo_util('get_selection_value')
def get_selection_value(report, model, field_name, field_val):
    selections = report.env[model].fields_get()[field_name]['selection']
    res = dict(selections)[field_val]
    return res


@aeroo_util('formatLang')
def format_lang(report, value, date=False, dp=False, currency_obj=False):
    if date:
        return format_date(report.env, value)
    else:
        return formatLang(report.env, value, dp=dp, currency_obj=currency_obj)


@aeroo_util('format_address')
def format_address(report, partner_id, address_type=None):

    if partner_id and address_type:
        contact_id = partner_id.address_get().get(address_type, False)
        if contact_id:
            partner_id = partner_id.env['res.partner'].browse(contact_id)

    # Create a basic object to store local variables accessible
    # from nested functions
    renderer = SimpleNamespace()
    renderer.result = ''
    renderer.newline = False
    renderer.last_level = 0

    def add_new_line(level):
        if renderer.newline and level > renderer.last_level:
            while renderer.newline:
                renderer.last_level = level
                renderer.result += '\n'
                if isinstance(renderer.newline, int):
                    renderer.newline -= 1
                else:
                    renderer.newline = False

    if partner_id:
        if partner_id.commercial_company_name:
            add_new_line(1)
            renderer.result += partner_id.commercial_company_name
            renderer.newline = True

        if partner_id.name != partner_id.commercial_company_name:
            if partner_id.title:
                add_new_line(1)
                renderer.result += partner_id.title.name + ' '
                renderer.newline = True
            if partner_id.name:
                add_new_line(1)
                renderer.result += partner_id.name
                renderer.newline = True

        if partner_id.street:
            add_new_line(2)
            renderer.result += partner_id.street
            renderer.newline = True
        if partner_id.street2:
            add_new_line(3)
            renderer.result += partner_id.street2
            renderer.newline = True
        if partner_id.zip:
            add_new_line(4)
            renderer.result += partner_id.zip + ' '
            renderer.newline = True
        if partner_id.city:
            add_new_line(4)
            renderer.result += partner_id.city.upper()
            renderer.newline = True
        if partner_id.state_id:
            add_new_line(5)
            renderer.result += partner_id.state_id.name.upper() + ' '
            renderer.newline = True
        if partner_id.country_id:
            add_new_line(5)
            renderer.result += partner_id.country_id.name.upper()
            renderer.newline = True
        renderer.newline = 2
        if partner_id.phone:
            add_new_line(6)
            renderer.result += u'Tél.: ' + partner_id.phone
            renderer.newline = True
        if partner_id.fax:
            add_new_line(7)
            renderer.result += 'Fax: ' + partner_id.fax
            renderer.newline = True
    if partner_id and partner_id.vat:
        add_new_line(8)
        renderer.result += 'TVA: ' + partner_id.vat

    return renderer.result


@aeroo_util('format_footer')
def format_footer(report, company_id):
    r = []
    if company_id:
        if company_id.report_footer:
            r.append('{}'.format(company_id.report_footer))
        if company_id.siret:
            r.append(_('SIRET {}').format(company_id.siret))
        if company_id.ape:
            r.append(_('APE {}').format(company_id.ape))
        if company_id.vat:
            r.append(_('VAT {}').format(company_id.vat))
        res = ' - '.join(r)
        return res


@aeroo_util('print_address_type')
def print_address_type(report, address_type):
    result = 'Adresse:'
    if address_type == 'invoice':
        result = 'Adresse de facturation:'
    if address_type == 'delivery':
        result = 'Adresse de livraison:'
    if address_type == 'contact':
        result = 'Adresse de contact:'
    return result