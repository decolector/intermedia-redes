# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Queries a table using the primary key or a secondary index.
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

class Query(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Query Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Query, self).__init__(temboo_session, '/Library/Amazon/DynamoDB/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

class QueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Query
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(QueryInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(QueryInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ConsistentRead(self, value):
        """
        Set the value of the ConsistentRead input for this Choreo. ((optional, boolean) Determines the read consistency model: If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.)
        """
        super(QueryInputSet, self)._set_input('ConsistentRead', value)
    def set_ExclusiveStartKey(self, value):
        """
        Set the value of the ExclusiveStartKey input for this Choreo. ((optional, json) The primary key of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedKey in the previous operation.)
        """
        super(QueryInputSet, self)._set_input('ExclusiveStartKey', value)
    def set_ExpressionAttributeNames(self, value):
        """
        Set the value of the ExpressionAttributeNames input for this Choreo. ((optional, json) One or more substitution tokens for attribute names in an expression.)
        """
        super(QueryInputSet, self)._set_input('ExpressionAttributeNames', value)
    def set_ExpressionAttributeValues(self, value):
        """
        Set the value of the ExpressionAttributeValues input for this Choreo. ((conditional, json) One or more values that can be substituted in an expression.)
        """
        super(QueryInputSet, self)._set_input('ExpressionAttributeValues', value)
    def set_FilterExpression(self, value):
        """
        Set the value of the FilterExpression input for this Choreo. ((optional, string) A string that contains conditions that DynamoDB applies after the Query operation, but before the data is returned to you.)
        """
        super(QueryInputSet, self)._set_input('FilterExpression', value)
    def set_IndexName(self, value):
        """
        Set the value of the IndexName input for this Choreo. ((optional, string) The name of an index to query. This index can be any local secondary index or global secondary index on the table.)
        """
        super(QueryInputSet, self)._set_input('IndexName', value)
    def set_KeyConditionExpression(self, value):
        """
        Set the value of the KeyConditionExpression input for this Choreo. ((conditional, string) The condition that specifies the key value(s) for items to be retrieved by the Query action.)
        """
        super(QueryInputSet, self)._set_input('KeyConditionExpression', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The maximum number of items to evaluate (not necessarily the number of matching items).)
        """
        super(QueryInputSet, self)._set_input('Limit', value)
    def set_ProjectionExpression(self, value):
        """
        Set the value of the ProjectionExpression input for this Choreo. ((optional, string) A string that identifies one or more attributes to retrieve from the table.)
        """
        super(QueryInputSet, self)._set_input('ProjectionExpression', value)
    def set_ReturnConsumedCapacity(self, value):
        """
        Set the value of the ReturnConsumedCapacity input for this Choreo. ((optional, string) Determines the level of detail about provisioned throughput consumption that is returned in the response. Valid values are: INDEXES, TOTAL, NONE.)
        """
        super(QueryInputSet, self)._set_input('ReturnConsumedCapacity', value)
    def set_ScanIndexForward(self, value):
        """
        Set the value of the ScanIndexForward input for this Choreo. ((optional, boolean) Specifies the order for index traversal: If true (default), the traversal is performed in ascending order; if false, the traversal is performed in descending order.)
        """
        super(QueryInputSet, self)._set_input('ScanIndexForward', value)
    def set_Select(self, value):
        """
        Set the value of the Select input for this Choreo. ((optional, string) The attributes to be returned in the result. Valid values are: ALL_ATTRIBUTES, ALL_PROJECTED_ATTRIBUTES, SPECIFIC_ATTRIBUTES, and COUNT.)
        """
        super(QueryInputSet, self)._set_input('Select', value)
    def set_TableName(self, value):
        """
        Set the value of the TableName input for this Choreo. ((required, string) The name of the table containing the requested items.)
        """
        super(QueryInputSet, self)._set_input('TableName', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the S3 endpoint you wish to access. The default region is "us-east-1".)
        """
        super(QueryInputSet, self)._set_input('UserRegion', value)

class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Amazon.)
        """
        return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
