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

import rx
from injector import singleton, inject
from rx import Observable

from gst.model.system_info import SystemInfo
from gst.repository.proc_cpuinfo_repository import ProcCpuinfoRepository

_LOG = logging.getLogger(__name__)


@singleton
class LoadProcCpuinfoInteractor:
    @inject
    def __init__(self, proc_cpuinfo_repository: ProcCpuinfoRepository) -> None:
        self._proc_cpuinfo_repository = proc_cpuinfo_repository

    def execute(self, system_info: SystemInfo) -> Observable:
        return rx.defer(lambda _: rx.just(self._proc_cpuinfo_repository.refresh(system_info)))
