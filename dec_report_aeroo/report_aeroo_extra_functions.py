# Copyright (C) DEC SARL, Inc - All Rights Reserved.
#
# CONFIDENTIAL NOTICE: Unauthorized copying and/or use of this file,
# via any medium is strictly prohibited.
# All information contained herein is, and remains the property of
# DEC SARL and its suppliers, if any.
# The intellectual and technical concepts contained herein are
# proprietary to DEC SARL and its suppliers and may be covered by
# French Law and Foreign Patents, patents in process, and are
# protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from DEC SARL.
# Written by Yann Papouin <y.papouin@dec-industrie.com>, Mar 2020

from odoo import _
from odoo.addons.report_aeroo.extra_functions import aeroo_util
from odoo.tools.misc import formatLang, format_date


@aeroo_util('formatLang')
def format_lang(report, value, date=False, dp=False, currency_obj=False):
    if date:
        return format_date(report.env, value)
    else:
        return formatLang(report.env, value, dp=dp, currency_obj=currency_obj)


@aeroo_util('format_address')
def format_address(report, partner_id):

    # Create a static class to store local variables accessible
    # from nested functions
    class local:
        result = ''
        newline = False
        last_level = 0

    def add_new_line(level):
        if local.newline and level > local.last_level:
            while local.newline:
                local.last_level = level
                local.result += '\n'
                if isinstance(local.newline, int):
                    local.newline -= 1
                else:
                    local.newline = False

    if partner_id:
        if partner_id.commercial_company_name:
            add_new_line(1)
            local.result += partner_id.commercial_company_name
            local.newline = True

        if partner_id.name != partner_id.commercial_company_name:
            if partner_id.title:
                add_new_line(1)
                local.result += partner_id.title.name + ' '
                local.newline = True
            if partner_id.name:
                add_new_line(1)
                local.result += partner_id.name
                local.newline = True

        if partner_id.street:
            add_new_line(2)
            local.result += partner_id.street
            local.newline = True
        if partner_id.street2:
            add_new_line(3)
            local.result += partner_id.street2
            local.newline = True
        if partner_id.zip:
            add_new_line(4)
            local.result += partner_id.zip + ' '
            local.newline = True
        if partner_id.city:
            add_new_line(4)
            local.result += partner_id.city.upper()
            local.newline = True
        if partner_id.state_id:
            add_new_line(5)
            local.result += partner_id.state_id.name.upper() + ' '
            local.newline = True
        if partner_id.country_id:
            add_new_line(5)
            local.result += partner_id.country_id.name.upper()
            local.newline = True
        local.newline = 2
        if partner_id.phone:
            add_new_line(6)
            local.result += u'Tél.: ' + partner_id.phone
            local.newline = True
        if partner_id.fax:
            add_new_line(7)
            local.result += 'Fax: ' + partner_id.fax
            local.newline = True
    if partner_id and partner_id.vat:
        add_new_line(8)
        local.result += 'TVA: ' + partner_id.vat

    return local.result


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
