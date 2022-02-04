# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2022

import json
from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def get_qrcode_data(self):
        self.ensure_one()
        # In contrary to the `product.template` implementation, we set the
        # `vid` property instead of `id` to differentiate labels
        res = {
            "vid": self.id,
            "code": self.default_code,
            "categ": {
                "id": self.categ_id.id,
            }
        }
        return json.dumps(res)

    def get_manufacturer(self):
        self.ensure_one()
        return self.product_tmpl_id.get_manufacturer()
