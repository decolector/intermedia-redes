# -*- coding: utf-8 -*-

###############################################################################
#
# ListMyActivities
# Returns a list of activity events for the authenticated user.
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

class ListMyActivities(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMyActivities Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListMyActivities, self).__init__(temboo_session, '/Library/YouTube/Activities/ListMyActivities')


    def new_input_set(self):
        return ListMyActivitiesInputSet()

    def _make_result_set(self, result, path):
        return ListMyActivitiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMyActivitiesChoreographyExecution(session, exec_id, path)

class ListMyActivitiesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMyActivities
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(ListMyActivitiesInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListMyActivitiesInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListMyActivitiesInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        super(ListMyActivitiesInputSet, self)._set_input('Fields', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        super(ListMyActivitiesInputSet, self)._set_input('MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "nextPageToken" found in the response which is used to page through results.)
        """
        super(ListMyActivitiesInputSet, self)._set_input('PageToken', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) Specifies a comma-separated list of one or more activity resource properties that the API response will include. Part names that you can pass are id, snippet, and contentDetails.)
        """
        super(ListMyActivitiesInputSet, self)._set_input('Part', value)
    def set_PublishedAfter(self, value):
        """
        Set the value of the PublishedAfter input for this Choreo. ((optional, date) Returns only results created after the specified time (formatted as a RFC 3339 date-time i.e. 1970-01-01T00:00:00Z).)
        """
        super(ListMyActivitiesInputSet, self)._set_input('PublishedAfter', value)
    def set_PublishedBefore(self, value):
        """
        Set the value of the PublishedBefore input for this Choreo. ((optional, date) Returns only results created before the specified time (formatted as a RFC 3339 date-time i.e. 1970-01-01T00:00:00Z).)
        """
        super(ListMyActivitiesInputSet, self)._set_input('PublishedBefore', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListMyActivitiesInputSet, self)._set_input('RefreshToken', value)

class ListMyActivitiesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMyActivities Choreo.
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
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from YouTube.)
        """
        return self._output.get('Response', None)

class ListMyActivitiesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListMyActivitiesResultSet(response, path)
