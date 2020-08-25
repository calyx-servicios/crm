##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    team_ids = fields.One2many('crm.team', 'user_id', 'Teams')