# This file is part of gst.
#
# Copyright (c) 2020 Roberto Leinardi
#
# gst is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gst is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gst.  If not, see <http://www.gnu.org/licenses/>.

import logging

LOG = logging.getLogger(__name__)
LOG_DEBUG_FORMAT = '%(filename)15s:%(lineno)-4d %(asctime)-15s: %(levelname)s/%(threadName)s(%(process)d) %(message)s'
LOG_INFO_FORMAT = '%(levelname)s: %(message)s'
LOG_WARNING_FORMAT = '%(message)s'


def set_log_level(level: int) -> None:
    log_format = LOG_WARNING_FORMAT
    if level <= logging.DEBUG:
        log_format = LOG_DEBUG_FORMAT
    elif level <= logging.INFO:
        log_format = LOG_INFO_FORMAT
    logging.basicConfig(level=level, format=log_format)
    logging.getLogger("Rx").setLevel(logging.INFO)
    logging.getLogger('injector').setLevel(logging.INFO)
    logging.getLogger('peewee').setLevel(logging.INFO)
    logging.getLogger('requests').setLevel(logging.INFO)
