# -*- coding: utf-8 -*-

###############################################################################
#
# BatchGetValues
# Returns one or more ranges of values from a spreadsheet.
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

class BatchGetValues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the BatchGetValues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(BatchGetValues, self).__init__(temboo_session, '/Library/Google/Sheets/BatchGetValues')


    def new_input_set(self):
        return BatchGetValuesInputSet()

    def _make_result_set(self, result, path):
        return BatchGetValuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BatchGetValuesChoreographyExecution(session, exec_id, path)

class BatchGetValuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the BatchGetValues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(BatchGetValuesInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(BatchGetValuesInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(BatchGetValuesInputSet, self)._set_input('ClientSecret', value)
    def set_DateTimeRenderOption(self, value):
        """
        Set the value of the DateTimeRenderOption input for this Choreo. ((optional, string) How dates, times, and durations should be represented in the output. Valid values are: SERIAL_NUMBER or FORMATTED_STRING. This is ignored if valueRenderOption is FORMATTED_VALUE.)
        """
        super(BatchGetValuesInputSet, self)._set_input('DateTimeRenderOption', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response. See Choreo notes for syntax details.)
        """
        super(BatchGetValuesInputSet, self)._set_input('Fields', value)
    def set_MajorDimension(self, value):
        """
        Set the value of the MajorDimension input for this Choreo. ((optional, string) Indicates the dimension that results should use. Valid values are ROWS (the default) or COLUMNS.)
        """
        super(BatchGetValuesInputSet, self)._set_input('MajorDimension', value)
    def set_Ranges(self, value):
        """
        Set the value of the Ranges input for this Choreo. ((required, string) The A1 notation of the values to retrieve formatted as an array (e.g. ["Sheet1!A2:C3"]). Note, this input supports up to 10 ranges.)
        """
        super(BatchGetValuesInputSet, self)._set_input('Ranges', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(BatchGetValuesInputSet, self)._set_input('RefreshToken', value)
    def set_SpreadsheetID(self, value):
        """
        Set the value of the SpreadsheetID input for this Choreo. ((required, string) The ID of the spreadsheet. This can be found in the URL when viewing your spreadsheet in your web browser.)
        """
        super(BatchGetValuesInputSet, self)._set_input('SpreadsheetID', value)
    def set_ValueRenderOption(self, value):
        """
        Set the value of the ValueRenderOption input for this Choreo. ((optional, string) How values should be represented in the output. Valid values are: FORMATTED_VALUE, UNFORMATTED_VALUE, or FORMULA.)
        """
        super(BatchGetValuesInputSet, self)._set_input('ValueRenderOption', value)

class BatchGetValuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the BatchGetValues Choreo.
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

class BatchGetValuesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return BatchGetValuesResultSet(response, path)
