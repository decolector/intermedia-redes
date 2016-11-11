# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateTable
# Modifies the provisioned throughput settings, global secondary indexes, or DynamoDB Streams settings for a given table.
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

class UpdateTable(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateTable Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateTable, self).__init__(temboo_session, '/Library/Amazon/DynamoDB/UpdateTable')


    def new_input_set(self):
        return UpdateTableInputSet()

    def _make_result_set(self, result, path):
        return UpdateTableResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateTableChoreographyExecution(session, exec_id, path)

class UpdateTableInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateTable
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UpdateTableInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UpdateTableInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AttributeDefinitions(self, value):
        """
        Set the value of the AttributeDefinitions input for this Choreo. ((optional, json) An array of attributes that describe the key schema for the table and indexes.)
        """
        super(UpdateTableInputSet, self)._set_input('AttributeDefinitions', value)
    def set_GlobalSecondaryIndexUpdates(self, value):
        """
        Set the value of the GlobalSecondaryIndexUpdates input for this Choreo. ((conditional, json) One or more global secondary indexes (the maximum is five) to be created on the table.)
        """
        super(UpdateTableInputSet, self)._set_input('GlobalSecondaryIndexUpdates', value)
    def set_ProvisionedThroughput(self, value):
        """
        Set the value of the ProvisionedThroughput input for this Choreo. ((conditional, json) Represents the provisioned throughput settings for a specified table or index.)
        """
        super(UpdateTableInputSet, self)._set_input('ProvisionedThroughput', value)
    def set_StreamSpecification(self, value):
        """
        Set the value of the StreamSpecification input for this Choreo. ((conditional, json) The settings for DynamoDB Streams on the table.)
        """
        super(UpdateTableInputSet, self)._set_input('StreamSpecification', value)
    def set_TableName(self, value):
        """
        Set the value of the TableName input for this Choreo. ((required, string) The name of the table to create.)
        """
        super(UpdateTableInputSet, self)._set_input('TableName', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the S3 endpoint you wish to access. The default region is "us-east-1".)
        """
        super(UpdateTableInputSet, self)._set_input('UserRegion', value)

class UpdateTableResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateTable Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateTableChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateTableResultSet(response, path)
