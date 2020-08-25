#############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re
import logging
_logger = logging.getLogger(__name__)


class OpportunityReport(models.Model):
	_inherit = "crm.opportunity.report"

	profit = fields.Float(string="Profit")
	planned_profit = fields.Float(string="Planed profit")

	def _select(self):
		select_str = super(OpportunityReport, self)._select()
		select_str = select_str+',\n c.profit, \nc.planned_profit'
		print(select_str)
		# asd = asd
		return select_str