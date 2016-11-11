# -*- coding: utf-8 -*-

###############################################################################
#
# BatchWriteItem
# Puts or deletes multiple items in one or more tables.
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

class BatchWriteItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the BatchWriteItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(BatchWriteItem, self).__init__(temboo_session, '/Library/Amazon/DynamoDB/BatchWriteItem')


    def new_input_set(self):
        return BatchWriteItemInputSet()

    def _make_result_set(self, result, path):
        return BatchWriteItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BatchWriteItemChoreographyExecution(session, exec_id, path)

class BatchWriteItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the BatchWriteItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(BatchWriteItemInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(BatchWriteItemInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_RequestItems(self, value):
        """
        Set the value of the RequestItems input for this Choreo. ((required, json) A map of one or more table names and, for each table, a list of operations to be performed (DeleteRequest or PutRequest). See choreo notes for more details.)
        """
        super(BatchWriteItemInputSet, self)._set_input('RequestItems', value)
    def set_ReturnConsumedCapacity(self, value):
        """
        Set the value of the ReturnConsumedCapacity input for this Choreo. ((optional, string) Determines the level of detail about provisioned throughput consumption that is returned in the response. Valid values are: INDEXES, TOTAL, NONE.)
        """
        super(BatchWriteItemInputSet, self)._set_input('ReturnConsumedCapacity', value)
    def set_ReturnItemCollectionMetrics(self, value):
        """
        Set the value of the ReturnItemCollectionMetrics input for this Choreo. ((optional, string) Determines whether item collection metrics are returned. Valid values are: SIZE and NONE.)
        """
        super(BatchWriteItemInputSet, self)._set_input('ReturnItemCollectionMetrics', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the S3 endpoint you wish to access. The default region is "us-east-1".)
        """
        super(BatchWriteItemInputSet, self)._set_input('UserRegion', value)

class BatchWriteItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the BatchWriteItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Amazon.)
        """
        return self._output.get('Response', None)

class BatchWriteItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return BatchWriteItemResultSet(response, path)
