# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#             <contact@eficent.com>
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
    "name": "Project progress measurement",
    "version": "1.0",
    "author": "Eficent",
    "website": "www.eficent.com",
    "category": "Generic Modules",
    "depends": ["project", "progress_measurement", "project_wbs"],
    "description": """
Project progress measurement.
====================================
    The progress of a project indicates the degree of completion, with respect to the estimated scope of work.
    Generally the progress cannot be automatically measured and it is based on the expert judgement or the
    completion of checklists that determine the degree of completion of a project.

Define Project Progress Measurements:
------------------------------------
    Project Progress Measurements record the results of the measurement on a project.
    A Progress Measurement is defined by the following attributes:
        * Project
        * Date: When the measurement occurred
        * Progress Type
        * Value: Results of the measurement. Must be defined in the precision indicated by the progress type.
        The user cannot enter a value that exceeds the maximum permitted value for that progress type.
        * Description: description of the measurement
        * Entered by: User that entered the measurement
    """,
    "init_xml": [],
    "update_xml": [
        "project_progress_measurement_view.xml",
        "wizard/progress_measurements_entry_view.xml",
        "project_project_view.xml",
        "security/ir.model.access.csv",
    ],
    'demo_xml': [

    ],
    'test':[
    ],
    'installable': True,
    'active': False,
    'certificate': '',
    'application': True,
}
