# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import header
import webtest


def test_send_mail(testbed):
    testbed.init_mail_stub()
    testbed.init_app_identity_stub()
    app = webtest.TestApp(header.app)
    response = app.post('/header', 'thread_id=42')
    assert response.status_int == 200
    assert ('Sent an email to Albert with Reference header set to 42.'
            in response.body)