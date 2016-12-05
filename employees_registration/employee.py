# -*- coding: utf-8 -*-

#    Bashir Idirs (Alsuty)
#    Copyright (C) 2016.
#
#    This Code is free: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


from openerp import models,fields, api

class Employee(models.Model):
	_name= 'employees.employee'

	name = fields.Char('Name')
	email = fields.Char('Email')
	department = fields.Selection(string="Department", 
						selection=[('general', 'General'), 
						('newtwork', 'Newtwork'), 
						('software', 'Software'),])

	#Override create method and do your change
	@api.model
	def create(self, vals):
		#Your change here
		emp = super(Employee, self).create(vals)
		#And/or here
		return emp 

	#Override write method and do your change here
	@api.multi
	def write(self, vals):
		#Do any thing here
		emp = super(Employee, self).write(vals)
		#And/or here 
		return emp

	#Override default_get to do your change
	@api.model
	def default_get(self, vals):
		emp = super(Employee, self).default_get(vals)
		return emp

	#Also you can override browse method to make some change
	@api.model
	def broswe(self, vals):
		#Your custom code here
		result = super(Employee, self).broswe(vals)
		#And/or here
		return result


