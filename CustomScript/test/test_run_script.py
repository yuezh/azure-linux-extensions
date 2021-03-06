#!/usr/bin/env python
#
#CustomScript extension
#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.6+
#

import unittest
import env
import os
import tempfile
from MockUtil import MockUtil
import customscript as cs

class TestCommandExecution(unittest.TestCase):
    def test_parse_cmd(self):
        print __file__
        cmd = u'sh foo.bar.sh -af bar --foo=bar | more \u6211'
        args = cs.parse_args(cmd.encode('utf-8'))
        self.assertNotEquals(None, args)
        self.assertNotEquals(0, len(args))
        print args
    
    def test_tail(self):
        with open("/tmp/testtail", "w+") as F:
            F.write(u"abcdefghijklmnopqrstu\u6211vwxyz".encode("utf-8"))
        tail = cs.tail("/tmp/testtail", 2)
        self.assertEquals("yz", tail)

        tail = cs.tail("/tmp/testtail")
        self.assertEquals("abcdefghijklmnopqrstuvwxyz", tail)

    def test_run_script(self):
        hutil = MockUtil(self)
        test_script = "mock.sh"
        os.chdir(os.path.join(env.root, "test"))
        cs.run_script(hutil, ["sh", test_script, "0"], 0.1)
        cs.run_script(hutil, ["sh", test_script, "1"], 0.1)

if __name__ == '__main__':
    unittest.main()
