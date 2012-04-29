#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

# Copyright Miguel Angel Garcia <miguelangel.garcia@gmail.com>

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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from freshen import *
from freshen.checks import *
import subprocess
import shlex

@Before
def setUp(sc):
    scc.pattern = None
    scc.current = None
    scc.status = None
    scc.output = None

@Given('two PDFs, (.*) and (.*)$')
def setArguments(pattern, current):
    scc.pattern = pattern
    scc.current = current

@When('I run exactly pdfcompare (.*)$')
def run_exactly(args):
    args_list = shlex.split(args)
    cmd = ['./lib/pdfcompare.py'] + args_list
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    scc.output, _ = process.communicate()
    scc.status = process.returncode

@When('I run pdfcompare over them')
def run():
    cmd = './lib/pdfcompare.py'
    arg1 = 'tests/patterns/{}'.format(scc.pattern)
    arg2 = 'tests/patterns/{}'.format(scc.current)
    process = subprocess.Popen([cmd, arg1, arg2], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    scc.output, _ = process.communicate()
    scc.status = process.returncode

@Then('the status is (\d+)')
def check_status(status):
    assert_equals(int(status), scc.status)

@Then('the output contains "(.+)"')
def check_output(output):
    if not output in scc.output:
        assert_true(False, 'Text "{}" was not found in {}'.format(output, scc.output))
