# -*- coding: utf-8 -*-

###############################################################################
#
# AddRow
# Adds rows to a table in a dataset
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

class AddRow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddRow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddRow, self).__init__(temboo_session, '/Library/Microsoft/PowerBI/AddRow')


    def new_input_set(self):
        return AddRowInputSet()

    def _make_result_set(self, result, path):
        return AddRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddRowChoreographyExecution(session, exec_id, path)

class AddRowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddRow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Rows(self, value):
        """
        Set the value of the Rows input for this Choreo. ((required, json) A JSON object contain one or more rows to insert into a Power BI table. See Choreo notes for formatting details.)
        """
        super(AddRowInputSet, self)._set_input('Rows', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This can be passed if your application is authenticating multiple Power BI users.)
        """
        super(AddRowInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Power BI. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(AddRowInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Power BI. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(AddRowInputSet, self)._set_input('ClientSecret', value)
    def set_DatasetID(self, value):
        """
        Set the value of the DatasetID input for this Choreo. ((required, string) The ID of the dataset that your table belongs to.)
        """
        super(AddRowInputSet, self)._set_input('DatasetID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your Power BI password. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(AddRowInputSet, self)._set_input('Password', value)
    def set_TableName(self, value):
        """
        Set the value of the TableName input for this Choreo. ((required, string) The name of the Power BI table to insert a row into.)
        """
        super(AddRowInputSet, self)._set_input('TableName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) Your Power BI username. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(AddRowInputSet, self)._set_input('Username', value)

class AddRowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddRow Choreo.
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

class AddRowChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddRowResultSet(response, path)
