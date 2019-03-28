# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2018 Maciej Kamiński (kaminski.maciej@gmail.com) Politechnika Wrocławska
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
###############################################################################
__author__ = 'Maciej Kamiński Politechnika Wrocławska'

from os import path
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from .dendryt import Dendryt

class DendrytPlugin(object):
    def __init__(self,iface):
        self.iface=iface
        self.plugin_path=path.dirname(path.abspath(__file__))
        self.icon_path=path.join(self.plugin_path,'images','cluster_icon.png')
        self.qicon=QIcon(self.icon_path)
        self.plugin_menu_entry="&Dendryt"
        self.menu_actions=[]
        #adding actions
        self.menu_actions.append(Dendryt(self))


    def initGui(self):
        """
        Gui initialization and actions adding
        """
        for action in self.menu_actions:
            self.iface.addPluginToMenu(self.plugin_menu_entry,action)
            self.iface.addToolBarIcon(action)

    def unload(self):
        """
        Gui purge
        """
        for action in self.menu_actions:
            self.iface.removePluginMenu(self.plugin_menu_entry,action)
            self.iface.removeToolBarIcon(action)

    def ui_loader(self,*ui_name):
        """
        Returns object created based on provided .ui filename.
        In addition subdirectory can be stated:
        ui_loader('form.ui')
        ui_loader('formsdir','form.ui')
        """
        return uic.loadUi(path.join(self.plugin_path,*ui_name))
