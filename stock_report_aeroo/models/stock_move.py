# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Aug 2020

from odoo import models, api, fields


class StockMove(models.Model):
    _inherit = [
        'stock.move',
        'report.line.mixin',
    ]
    _name = 'stock.move'
