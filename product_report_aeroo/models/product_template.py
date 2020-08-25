# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Aug 2020

from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def _get_aeroo_report_filename(self):
        names = [x.name for x in self]
        res = '-'.join(names)
        return res
