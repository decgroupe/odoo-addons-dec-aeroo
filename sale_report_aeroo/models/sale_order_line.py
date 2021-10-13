# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2020

from odoo import models


class SaleOrderLine(models.Model):
    _inherit = [
        'sale.order.line',
        'report.line.mixin',
        'report.orderline.mixin',
    ]
    _name = 'sale.order.line'
