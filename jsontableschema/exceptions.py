# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class InvalidSchemaError(Exception):
    def __init__(self, msg=None):
        self.msg = msg or 'The obj is not a valid JSON Table Schema.'


class InvalidJSONError(Exception):
    def __init__(self, msg=None):
        self.msg = msg or 'The obj cannot be parsed as JSON.'


class ConstraintError(Exception):
    def __init__(self, msg=None):
        self.msg = msg or "The value didn't validate against a constraint."


class ConstraintNotSupported(Exception):
    def __init__(self, msg=None):
        self.msg = msg or "The field does not support the constraint."
