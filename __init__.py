# -*- coding: utf-8 -*-
#
# Copyright (c) 2007 by BlueDynamics Alliance, Austria
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plaintext' 

import logging
logger = logging.getLogger('UserAndGroupSelectionWidget')
logger.info('Installing Product')

from widget import UserAndGroupSelectionWidget
from Products.CMFCore.DirectoryView import registerDirectory
from config import GLOBALS
registerDirectory('skins', GLOBALS)