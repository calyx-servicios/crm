##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import re
import logging
_logger = logging.getLogger(__name__)


class Lead(models.Model):
	_inherit = "crm.lead"

	@api.model
	def _default_currency(self):
		return self.env.ref('base.USD').id

	currency_id = fields.Many2one('res.currency', string='Currency',
		required=True, default=_default_currency, track_visibility='always', readonly=True)
