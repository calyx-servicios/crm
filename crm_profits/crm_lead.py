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


	@api.onchange('profit', 'planned_revenue')
	def profit_onchange(self):
	        try:
	         	self.planned_profit = self.profit * self.planned_revenue / 100
	        except:
	             raise "Error"
	
	@api.onchange('planned_profit')
	def planned_profit_onchange(self):
	        try:
	         	self.profit = self.planned_profit * 100  / self.planned_revenue
	        except:
	             raise "Error"
	            
	            
	profit = fields.Float(string="Profit")
	planned_profit = fields.Float(string="Planed profit")
