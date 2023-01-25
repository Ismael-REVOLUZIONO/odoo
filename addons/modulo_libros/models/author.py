# -*- coding: utf-8 -*-
from odoo import models, fields, api


class author(models.Model):
    _name = 'authoroo'

    name  = fields.Char('Nombre Author')