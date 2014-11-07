# -*- coding: utf-8 -*-
################################################################
#    License, author and contributors information in:          #
#    __openerp__.py file at the root folder of this module.    #
################################################################

from openerp.osv import fields, orm


class res_partner(orm.Model):
    # Just inherit the res.partner model (from 'base' module)
    _inherit = "res.partner"
    
    # We add two very simple boolean fields, extending the model
    _columns = {
        'trainer': fields.boolean('Trainer',
                          help="Check this box if this contact is a trainer."),
        'trainee': fields.boolean('Trainee',
                          help="Check this box if this contact is a trainee."),        
    }
    
    # If we want to initialize field 'trainee' to True by default, we can do:
    _defaults = {  
        'trainee': True, 
    }
