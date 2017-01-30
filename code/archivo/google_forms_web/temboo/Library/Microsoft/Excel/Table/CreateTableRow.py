# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTableRow
# Creates new rows in a table.
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

class CreateTableRow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateTableRow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateTableRow, self).__init__(temboo_session, '/Library/Microsoft/Excel/Table/CreateTableRow')


    def new_input_set(self):
        return CreateTableRowInputSet()

    def _make_result_set(self, result, path):
        return CreateTableRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTableRowChoreographyExecution(session, exec_id, path)

class CreateTableRowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateTableRow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Values(self, value):
        """
        Set the value of the Values input for this Choreo. ((required, json) This is an array of arrays. The outer array can represent one or more rows while the inner array can represent one or more cell values. See Choreo notes below for more details.)
        """
        super(CreateTableRowInputSet, self)._set_input('Values', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This can be passed if your application is authenticating multiple Office 365 users.)
        """
        super(CreateTableRowInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Microsoft. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(CreateTableRowInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Microsoft. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(CreateTableRowInputSet, self)._set_input('ClientSecret', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Indicates that the row should be created at this index.)
        """
        super(CreateTableRowInputSet, self)._set_input('Index', value)
    def set_ItemPath(self, value):
        """
        Set the value of the ItemPath input for this Choreo. ((required, string) The location of the spreadsheet in OneDrive (e.g. MyFolder/Book.xlsx).)
        """
        super(CreateTableRowInputSet, self)._set_input('ItemPath', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your Microsoft password. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(CreateTableRowInputSet, self)._set_input('Password', value)
    def set_Table(self, value):
        """
        Set the value of the Table input for this Choreo. ((required, string) The name or id of the table to write to (e.g. Table1).)
        """
        super(CreateTableRowInputSet, self)._set_input('Table', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) Your Microsoft username. This is requried unless providing a valid AccessToken (see optional inputs).)
        """
        super(CreateTableRowInputSet, self)._set_input('Username', value)
    def set_Worksheet(self, value):
        """
        Set the value of the Worksheet input for this Choreo. ((required, string) The name or id of the worksheet to write to (e.g. Sheet1).)
        """
        super(CreateTableRowInputSet, self)._set_input('Worksheet', value)

class CreateTableRowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateTableRow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Microsoft.)
        """
        return self._output.get('Response', None)

class CreateTableRowChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateTableRowResultSet(response, path)
