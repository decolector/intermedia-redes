# -*- coding: utf-8 -*-

###############################################################################
#
# GetQueryResults
# Retrieves the results of a query with a given JobID when a query request times out and returns before the results are available.
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

class GetQueryResults(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetQueryResults Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetQueryResults, self).__init__(temboo_session, '/Library/Google/BigQuery/Jobs/GetQueryResults')


    def new_input_set(self):
        return GetQueryResultsInputSet()

    def _make_result_set(self, result, path):
        return GetQueryResultsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetQueryResultsChoreographyExecution(session, exec_id, path)

class GetQueryResultsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetQueryResults
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(GetQueryResultsInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(GetQueryResultsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(GetQueryResultsInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying which fields to include in a partial response.)
        """
        super(GetQueryResultsInputSet, self)._set_input('Fields', value)
    def set_JobID(self, value):
        """
        Set the value of the JobID input for this Choreo. ((required, string) Job ID of the query job.)
        """
        super(GetQueryResultsInputSet, self)._set_input('JobID', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) Maximum number of results to return. Defaults to 100. Max is 1000.)
        """
        super(GetQueryResultsInputSet, self)._set_input('MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) Page token, returned by a previous call, identifying the result set.)
        """
        super(GetQueryResultsInputSet, self)._set_input('PageToken', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, string) The ID of your Google API project.)
        """
        super(GetQueryResultsInputSet, self)._set_input('ProjectID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(GetQueryResultsInputSet, self)._set_input('RefreshToken', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) Zero-based index of the starting row to read.)
        """
        super(GetQueryResultsInputSet, self)._set_input('StartIndex', value)
    def set_TimeoutMs(self, value):
        """
        Set the value of the TimeoutMs input for this Choreo. ((optional, integer) How long to wait for the query to complete, in milliseconds, before returning. Default is 10000. If the timeout passes before the job completes, the 'jobComplete' field in the response will be false.)
        """
        super(GetQueryResultsInputSet, self)._set_input('TimeoutMs', value)

class GetQueryResultsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetQueryResults Choreo.
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

class GetQueryResultsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetQueryResultsResultSet(response, path)
