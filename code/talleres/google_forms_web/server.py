#!/usr/bin/Python
# -*- coding: latin-1 -*-
#Servidor temboo web
#Este es un simple servidor que hace de proxy o relevo
#entre una pagina web que usa el sdk de javascript de temboo
#y el servidor de temboo.
# Basado en un ejemplo de temboo.com
# Camilo Martinez
# cmart@decolector.net


from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File

from temboo.Library.Google.Sheets import GetValues
from temboo.core.session import TembooSession
from temboo.core.proxy import TembooProxy


class ProxyServer(Resource):
    def render_POST(self, request):
        print("Enviando petición a temboo")
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


#root representa la raiz del servidor o "/"
#este es el recurso principal a servir
root = Resource()
#agretamos el archivo index.html al recurso
root.putChild('', File('index.html'))
#Servimos el folder con ls sctips de javascript
root.putChild('js', File('js/'))
root.putChild('styles', File('styles/'))

#en la direccion /proxy-server esta el endpoint o
#recurso que se encarga de hacer la peticion a temboo.com
root.putChild('proxy-server', ProxyServer())

factory = Site(root)
#Se inicia el servidor en el puerto 8000
reactor.listenTCP(8000, factory)
print(
"Iniciando servidor en  \n"
+"Puede ver la página en la url: http://127.0.0.1:8000"
)
reactor.run()
