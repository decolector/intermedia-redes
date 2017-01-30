# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateItem
# Edits an existing item's attributes, or adds a new item to the table if it does not already exist.
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

class UpdateItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateItem, self).__init__(temboo_session, '/Library/Amazon/DynamoDB/UpdateItem')


    def new_input_set(self):
        return UpdateItemInputSet()

    def _make_result_set(self, result, path):
        return UpdateItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateItemChoreographyExecution(session, exec_id, path)

class UpdateItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UpdateItemInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UpdateItemInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ConditionExpression(self, value):
        """
        Set the value of the ConditionExpression input for this Choreo. ((optional, string) A condition that must be satisfied in order for a conditional update to succeed.)
        """
        super(UpdateItemInputSet, self)._set_input('ConditionExpression', value)
    def set_ExpressionAttributeNames(self, value):
        """
        Set the value of the ExpressionAttributeNames input for this Choreo. ((optional, json) One or more substitution tokens for attribute names in an expression.)
        """
        super(UpdateItemInputSet, self)._set_input('ExpressionAttributeNames', value)
    def set_ExpressionAttributeValues(self, value):
        """
        Set the value of the ExpressionAttributeValues input for this Choreo. ((optional, json) One or more values that can be substituted in an expression.)
        """
        super(UpdateItemInputSet, self)._set_input('ExpressionAttributeValues', value)
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, json) The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.)
        """
        super(UpdateItemInputSet, self)._set_input('Key', value)
    def set_ReturnConsumedCapacity(self, value):
        """
        Set the value of the ReturnConsumedCapacity input for this Choreo. ((optional, string) Determines the level of detail about provisioned throughput consumption that is returned in the response. Valid values are: INDEXES, TOTAL, NONE.)
        """
        super(UpdateItemInputSet, self)._set_input('ReturnConsumedCapacity', value)
    def set_ReturnItemCollectionMetrics(self, value):
        """
        Set the value of the ReturnItemCollectionMetrics input for this Choreo. ((optional, string) Determines whether item collection metrics are returned. Valid values are: SIZE and NONE.)
        """
        super(UpdateItemInputSet, self)._set_input('ReturnItemCollectionMetrics', value)
    def set_ReturnValues(self, value):
        """
        Set the value of the ReturnValues input for this Choreo. ((optional, string) Use ReturnValues if you want to get the item attributes as they appeared either before or after they were updated. Valid values are NONE and ALL_OLD.)
        """
        super(UpdateItemInputSet, self)._set_input('ReturnValues', value)
    def set_TableName(self, value):
        """
        Set the value of the TableName input for this Choreo. ((required, string) The name of the table to contain the item.)
        """
        super(UpdateItemInputSet, self)._set_input('TableName', value)
    def set_UpdateExpression(self, value):
        """
        Set the value of the UpdateExpression input for this Choreo. ((optional, string) An expression that defines one or more attributes to be updated, the action to be performed on them, and new value(s) for them.)
        """
        super(UpdateItemInputSet, self)._set_input('UpdateExpression', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the S3 endpoint you wish to access. The default region is "us-east-1".)
        """
        super(UpdateItemInputSet, self)._set_input('UserRegion', value)

class UpdateItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateItemResultSet(response, path)
