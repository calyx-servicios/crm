##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import models, fields, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    requested_date = fields.Datetime(string='Requested Date')
