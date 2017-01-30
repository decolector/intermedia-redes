# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateValues
# Updates values in the specified range of a spreadsheet.
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

class UpdateValues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateValues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateValues, self).__init__(temboo_session, '/Library/Google/Sheets/UpdateValues')


    def new_input_set(self):
        return UpdateValuesInputSet()

    def _make_result_set(self, result, path):
        return UpdateValuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateValuesChoreographyExecution(session, exec_id, path)

class UpdateValuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateValues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(UpdateValuesInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(UpdateValuesInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(UpdateValuesInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response. See Choreo notes for syntax details.)
        """
        super(UpdateValuesInputSet, self)._set_input('Fields', value)
    def set_MajorDimension(self, value):
        """
        Set the value of the MajorDimension input for this Choreo. ((optional, string) Indicates the dimension that the values array applies to. Valid values are ROWS (the default) or COLUMNS.)
        """
        super(UpdateValuesInputSet, self)._set_input('MajorDimension', value)
    def set_Range(self, value):
        """
        Set the value of the Range input for this Choreo. ((required, string) The A1 notation of a range to update. See Choreos notes for more details.)
        """
        super(UpdateValuesInputSet, self)._set_input('Range', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(UpdateValuesInputSet, self)._set_input('RefreshToken', value)
    def set_SpreadsheetID(self, value):
        """
        Set the value of the SpreadsheetID input for this Choreo. ((required, string) The ID of the spreadsheet. This can be found in the URL when viewing your spreadsheet in your web browser.)
        """
        super(UpdateValuesInputSet, self)._set_input('SpreadsheetID', value)
    def set_ValueInputOption(self, value):
        """
        Set the value of the ValueInputOption input for this Choreo. ((optional, string) Specifies how the input data should be interpreted. Valid values are: RAW (the default) and USER_ENTERED.)
        """
        super(UpdateValuesInputSet, self)._set_input('ValueInputOption', value)
    def set_Values(self, value):
        """
        Set the value of the Values input for this Choreo. ((required, json) This is an array of arrays. The outer array can represent one or more rows while the inner array can represent one or more cell values. See Choreo notes below for more details.)
        """
        super(UpdateValuesInputSet, self)._set_input('Values', value)

class UpdateValuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateValues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class UpdateValuesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateValuesResultSet(response, path)
