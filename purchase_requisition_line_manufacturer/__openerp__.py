# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
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
#
##############################################################################
{
    "name": "Purchase Requisition Line Manufacturer",
    "version": "1.0", 
    "author": "Eficent",
    "category": "", 
    "description": """
Purchase Requisition Line Manufacturer
======================================
This modules adds the manufacturer to the purchase requisitions

""", 
    "website": "http://www.eficent.com/",
    "license": "", 
    "depends": [
        "purchase_requisition",
        "product_manufacturer",
        "purchase_requisition_line_analytic",
    ], 
    "demo": [], 
    "data": [
        "view/purchase_requisition_view.xml"
    ], 
    "test": [], 
    "js": [], 
    "css": [], 
    "qweb": [], 
    "installable": True, 
    "auto_install": False, 
    "active": False
}