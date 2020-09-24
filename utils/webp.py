# -*- coding: utf-8 -*-

# 
# Copyright (C) 2020 Utopic Panther
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

import os
import subprocess

def cwebp(ofn, tfn):
    cp = subprocess.run(["cwebp", ofn, "-o", tfn], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if cp.returncode != 0:
        raise RuntimeError(f"cwebp {ofn} error, outputs:\n{cp.stdout.decode('utf-8')}")

allowed_suffixes = set(['.png', '.jpg', '.jpeg', '.tiff', '.webp'])

def can_convert(fn):
    suffix = os.path.splitext(fn)[1]
    return suffix in allowed_suffixes
