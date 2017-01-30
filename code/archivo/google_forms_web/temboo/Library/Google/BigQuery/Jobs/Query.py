# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Runs a BigQuery SQL query and returns results if the query completes within a specified timeout. When a query timeout occurs, results can be retrieved using the Job ID returned in the response.
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
        super(Query, self).__init__(temboo_session, '/Library/Google/BigQuery/Jobs/Query')


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
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(QueryInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(QueryInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(QueryInputSet, self)._set_input('ClientSecret', value)
    def set_DatasetID(self, value):
        """
        Set the value of the DatasetID input for this Choreo. ((optional, string) The ID of the dataset that your table belongs to.)
        """
        super(QueryInputSet, self)._set_input('DatasetID', value)
    def set_DryRun(self, value):
        """
        Set the value of the DryRun input for this Choreo. ((optional, boolean) If set to true, BigQuery doesn't run the job. Instead, if the query is valid, BigQuery returns statistics about the job such as how many bytes would be processed. Defaults to false.)
        """
        super(QueryInputSet, self)._set_input('DryRun', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying which fields to include in a partial response.)
        """
        super(QueryInputSet, self)._set_input('Fields', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) Maximum number of results to return. Defaults to 100. Max is 1000.)
        """
        super(QueryInputSet, self)._set_input('MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) Page token, returned by a previous call, identifying the result set.)
        """
        super(QueryInputSet, self)._set_input('PageToken', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, string) The ID of your Google API project.)
        """
        super(QueryInputSet, self)._set_input('ProjectID', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) A query to execute. Example: SELECT count(f1) FROM [myProjectId:myDatasetId.myTableId].)
        """
        super(QueryInputSet, self)._set_input('Query', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(QueryInputSet, self)._set_input('RefreshToken', value)
    def set_TimeoutMs(self, value):
        """
        Set the value of the TimeoutMs input for this Choreo. ((optional, integer) How long to wait for the query to complete, in milliseconds, before the request times out and returns. Defaults to 10000.)
        """
        super(QueryInputSet, self)._set_input('TimeoutMs', value)
    def set_UseQueryCache(self, value):
        """
        Set the value of the UseQueryCache input for this Choreo. ((optional, boolean) Whether to look for the result in the query cache. Defaults to true.)
        """
        super(QueryInputSet, self)._set_input('UseQueryCache', value)

class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
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

class QueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
