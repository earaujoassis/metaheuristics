# -*- coding: utf-8 -*-
# Copyright 2011-2015 Ewerton Assis
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Utils functions for the benchmark suite


import os


def folder_forward_slash(path):
    if not path.endswith('/'):
        path = "{0}/".format(path)
    return path


def mkdirp(directory):
    if not os.path.isdir(directory):
        os.system('mkdir -p {0}'.format(directory))
