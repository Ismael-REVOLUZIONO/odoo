# -*- coding: utf-8 -*-
from odoo import models, fields, api


class author(models.Model):
    _name = 'authorss'

    name  = fields.Char('Nombre Author')