# -*- coding: utf-8 -*-

###############################################################################
#
# GetItem
# Returns a set of attributes for the item with the given primary key.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetItem, self).__init__(temboo_session, '/Library/Amazon/DynamoDB/GetItem')


    def new_input_set(self):
        return GetItemInputSet()

    def _make_result_set(self, result, path):
        return GetItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetItemChoreographyExecution(session, exec_id, path)

class GetItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetItemInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetItemInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ConsistentRead(self, value):
        """
        Set the value of the ConsistentRead input for this Choreo. ((optional, boolean) Determines the read consistency model: If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.)
        """
        super(GetItemInputSet, self)._set_input('ConsistentRead', value)
    def set_ExpressionAttributeNames(self, value):
        """
        Set the value of the ExpressionAttributeNames input for this Choreo. ((optional, json) One or more substitution tokens for attribute names in an expression.)
        """
        super(GetItemInputSet, self)._set_input('ExpressionAttributeNames', value)
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, json) A map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve.)
        """
        super(GetItemInputSet, self)._set_input('Key', value)
    def set_ProjectionExpression(self, value):
        """
        Set the value of the ProjectionExpression input for this Choreo. ((optional, string) A string that identifies one or more attributes to retrieve from the table.)
        """
        super(GetItemInputSet, self)._set_input('ProjectionExpression', value)
    def set_ReturnConsumedCapacity(self, value):
        """
        Set the value of the ReturnConsumedCapacity input for this Choreo. ((optional, string) Determines the level of detail about provisioned throughput consumption that is returned in the response. Valid values are: INDEXES, TOTAL, NONE.)
        """
        super(GetItemInputSet, self)._set_input('ReturnConsumedCapacity', value)
    def set_TableName(self, value):
        """
        Set the value of the TableName input for this Choreo. ((required, string) The name of the table containing the requested items.)
        """
        super(GetItemInputSet, self)._set_input('TableName', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the S3 endpoint you wish to access. The default region is "us-east-1".)
        """
        super(GetItemInputSet, self)._set_input('UserRegion', value)

class GetItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetItemResultSet(response, path)
