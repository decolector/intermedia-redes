# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDataset
# Creates a new Dataset from a JSON schema definition and returns the Dataset ID and the properties of the dataset created.
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

class CreateDataset(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDataset Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateDataset, self).__init__(temboo_session, '/Library/Microsoft/PowerBI/CreateDataset')


    def new_input_set(self):
        return CreateDatasetInputSet()

    def _make_result_set(self, result, path):
        return CreateDatasetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDatasetChoreographyExecution(session, exec_id, path)

class CreateDatasetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDataset
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_SchemaDefinition(self, value):
        """
        Set the value of the SchemaDefinition input for this Choreo. ((required, json) A JSON object containing information about the dataset table and columns. See Choreo notes for formatting details.)
        """
        super(CreateDatasetInputSet, self)._set_input('SchemaDefinition', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This can be passed if your application is authenticating multiple Power BI users.)
        """
        super(CreateDatasetInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Power BI. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(CreateDatasetInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Power BI. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(CreateDatasetInputSet, self)._set_input('ClientSecret', value)
    def set_DefaultRetentionPolicy(self, value):
        """
        Set the value of the DefaultRetentionPolicy input for this Choreo. ((optional, string) Enables a default retention policy to automatically clean up old data while keeping a constant flow of new data going into your dashboard. Valid values are: None (the default) or basicFIFO.)
        """
        super(CreateDatasetInputSet, self)._set_input('DefaultRetentionPolicy', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your Power BI password. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(CreateDatasetInputSet, self)._set_input('Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) Your Power BI username. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(CreateDatasetInputSet, self)._set_input('Username', value)

class CreateDatasetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDataset Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseCode(self):
        """
        Retrieve the value for the "ResponseCode" output from this Choreo execution. ((integer) The response status code returned from Power BI.)
        """
        return self._output.get('ResponseCode', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Power BI.)
        """
        return self._output.get('Response', None)

class CreateDatasetChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateDatasetResultSet(response, path)
