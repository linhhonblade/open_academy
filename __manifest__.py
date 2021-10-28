# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Open Academy',
    'version': '1.1',
    'summary': 'Academy',
    'sequence': 10,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml'],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
