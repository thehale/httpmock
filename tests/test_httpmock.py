# Copyright (c) 2024 Joseph Hale
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import requests

import httpmock


@httpmock.enabled
def test_something():
    httpmock.on("GET", "http://example.com").respond(body="Hello, world!")
    assert requests.get("http://example.com").text == "Hello, world!"
