from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File

from temboo.Library.Google.Sheets import GetValues
from temboo.core.session import TembooSession
from temboo.core.proxy import TembooProxy

class ProxyServer(Resource):
    def render_POST(self, request):
        # Create a session with your Temboo account details
        session = TembooSession('almanaranja', 'MyFirstApp', '1LB6hWkQNaFcBYD7UhRsz2AxlRth6GUS')

        # Act as a proxy for the JS SDK
        tembooProxy = TembooProxy()

        # Instantiate the Choreo
        getValuesChoreo = GetValues(session)

        # Add Choreo proxy with an ID matching that specified by the JS SDK client
        tembooProxy.add_choreo('jsGetValues', getValuesChoreo)

        # Get an InputSet object for the Choreo
        getValuesInputs = getValuesChoreo.new_input_set()

        # Set credential to use for execution
        getValuesInputs.set_credential('GoogleSheetsAccount')

        tembooProxy.set_default_inputs('jsGetValues', getValuesInputs);

        # Whitelist inputs
        tembooProxy.allow_user_inputs('jsGetValues', 'Range')
        tembooProxy.allow_user_inputs('jsGetValues', 'SpreadsheetID')

        # Execute the requested Choreo. httpPostData contains the contents of the JavaScript client POST
        # request. How this variable is populated will depend on your Python web server implementation.
        result = tembooProxy.execute(request.args['temboo_proxy'][0])

        return result



root = Resource()
root.putChild('', File('index.html'))
root.putChild('js', File('js/'))
root.putChild('proxy-server', ProxyServer())

factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()
