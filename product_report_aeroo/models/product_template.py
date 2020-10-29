# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Aug 2020

import json
from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def _get_aeroo_report_filename(self):
        names = [x.name or str(x.id) for x in self]
        res = '-'.join(names)
        return res

    def get_qrcode_data(self):
        res = {
            "id": self.id,
            "code": self.default_code,
            "categ": {
                "id": self.categ_id.id,
            }
        }
        return json.dumps(res)

    def get_manufacturer(self):
        res = ''
        categ_id = self.categ_id
        if categ_id:
            while categ_id.parent_id and (categ_id.parent_id.id != 1):
                categ_id = categ_id.parent_id
            if categ_id != self.categ_id:
                res = ('%s - %s') % (categ_id.name, self.categ_id.name)
            else:
                res = ('%s') % (categ_id.name)
        return res
