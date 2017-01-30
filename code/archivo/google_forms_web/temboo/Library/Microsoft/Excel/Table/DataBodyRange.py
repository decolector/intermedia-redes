# -*- coding: utf-8 -*-

###############################################################################
#
# DataBodyRange
# Gets the range object associated with the data body of the table.
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

class DataBodyRange(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DataBodyRange Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DataBodyRange, self).__init__(temboo_session, '/Library/Microsoft/Excel/Table/DataBodyRange')


    def new_input_set(self):
        return DataBodyRangeInputSet()

    def _make_result_set(self, result, path):
        return DataBodyRangeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DataBodyRangeChoreographyExecution(session, exec_id, path)

class DataBodyRangeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DataBodyRange
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This can be passed if your application is authenticating multiple Office 365 users.)
        """
        super(DataBodyRangeInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Microsoft. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(DataBodyRangeInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Microsoft. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(DataBodyRangeInputSet, self)._set_input('ClientSecret', value)
    def set_ItemPath(self, value):
        """
        Set the value of the ItemPath input for this Choreo. ((required, string) The location of the spreadsheet in OneDrive (e.g. MyFolder/Book.xlsx).)
        """
        super(DataBodyRangeInputSet, self)._set_input('ItemPath', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your Microsoft password. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(DataBodyRangeInputSet, self)._set_input('Password', value)
    def set_Select(self, value):
        """
        Set the value of the Select input for this Choreo. ((optional, string) Comma-separated list of properties to include in the response.)
        """
        super(DataBodyRangeInputSet, self)._set_input('Select', value)
    def set_Table(self, value):
        """
        Set the value of the Table input for this Choreo. ((required, string) The name or id of the table.)
        """
        super(DataBodyRangeInputSet, self)._set_input('Table', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) Your Microsoft username. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(DataBodyRangeInputSet, self)._set_input('Username', value)
    def set_Worksheet(self, value):
        """
        Set the value of the Worksheet input for this Choreo. ((required, string) The name or id of the worksheet.)
        """
        super(DataBodyRangeInputSet, self)._set_input('Worksheet', value)

class DataBodyRangeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DataBodyRange Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Microsoft.)
        """
        return self._output.get('Response', None)

class DataBodyRangeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DataBodyRangeResultSet(response, path)
