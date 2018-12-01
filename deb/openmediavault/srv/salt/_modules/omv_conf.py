# -*- coding: utf-8 -*-
#
# This file is part of OpenMediaVault.
#
# @license   http://www.gnu.org/licenses/gpl.html GPL Version 3
# @author    Volker Theile <volker.theile@openmediavault.org>
# @copyright Copyright (c) 2009-2018 Volker Theile
#
# OpenMediaVault is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# OpenMediaVault is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OpenMediaVault. If not, see <http://www.gnu.org/licenses/>.
import openmediavault.config
import openmediavault.device
import os


def get(id_, identifier=None):
    db = openmediavault.config.Database()
    objs = db.get(id_, identifier)
    if isinstance(objs, list):
        return [obj.get_dict() for obj in objs]
    return objs.get_dict()


def get_by_filter(id_, filter_):
    db = openmediavault.config.Database()
    objs = db.get_by_filter(id_, openmediavault.config.DatabaseFilter(filter_))
    if isinstance(objs, list):
        return [obj.get_dict() for obj in objs]
    return objs.get_dict()


def get_sharedfolder_path(uuid):
    sf_obj = get('conf.system.sharedfolder', uuid)
    mp_obj = get('conf.system.filesystem.mountpoint', sf_obj['mntentref'])
    return os.path.join(mp_obj['dir'], sf_obj['reldirpath'])


def get_sharedfolder_name(uuid):
    sf_obj = get('conf.system.sharedfolder', uuid)
    return sf_obj['name']


def get_sharedfolder_mount_dir(uuid):
    sf_obj = get('conf.system.sharedfolder', uuid)
    mp_obj = get('conf.system.filesystem.mountpoint', sf_obj['mntentref'])
    return mp_obj['dir']
