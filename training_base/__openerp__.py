# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2014      Anubía, soluciones en la nube,SL (http://www.anubia.es)
#                      Alejandro Santana <alejandrosantana@anubia.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
##############################################################################

{
    'name': 'Module example: Training',
    'version': '0.1',
    'category': 'Training',
    'description': '''
This module is just an example for a training course
====================================================

    * This serves as an example on how to build an OpenERP 7.0 module.
    * Shows how to inherit and extend a model with custom variables.
    * Shows how to create views related to models.
    * Shows how to create top menus, left-side menus and submenus.
    * Shows how to create actions relating menus to views.
    * Shows how to create default filtering for views.
    * Shows how to use simple security definition xml file.
    * Shows how to create filter definitions to be used in views.

''',
    # 'complexity': 'normal',
    'license': 'AGPL-3',
    'author': 'Alejandro Santana <alejandrosantana@anubia.es>',
    'maintainer': 'Anubía, soluciones en la nube, SL',
    'website': 'http://www.anubia.es',
    'contributors': [
        'Alejandro Santana <alejandrosantana@anubia.es>"',
    ],
    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'security/security.xml', 
        'training_base_view.xml',
        'res_partner_view.xml',
     ],
    'demo': [],
    'test': [],
    'images': [],
    'css': [],
    'js': [],
    'installable': True,
    'application': False,
    'auto_install': False,
#    'certificate': 'certificate',
}
