import com.temboo.core.*;

import com.temboo.Library.Google.Spreadsheets.*;

// Create a session using your Temboo account application details
TembooSession session = new TembooSession("user", "app-name", "key");



void setup() {

  // Run the RetrieveSpecificRowsOrColumns Choreo function
  runRetrieveSpecificRowsOrColumnsChoreo();
}


//Realiza la peticion de filas o columnas
void runRetrieveSpecificRowsOrColumnsChoreo() {

  // Create the Choreo object using your Temboo session
  RetrieveSpecificRowsOrColumns retrieveSpecificRowsOrColumnsChoreo = new RetrieveSpecificRowsOrColumns(session);



  // Set credential
  retrieveSpecificRowsOrColumnsChoreo.setCredential("mySpreadsheet");



  // Set inputs
  // Run the Choreo and store the results

  RetrieveSpecificRowsOrColumnsResultSet retrieveSpecificRowsOrColumnsResults = retrieveSpecificRowsOrColumnsChoreo.run();
  // Print results
  XML xml = parseXML(retrieveSpecificRowsOrColumnsResults.getResponse());
  
  parseResults(xml);
  //println(retrieveSpecificRowsOrColumnsResults.getResponse());
  println(retrieveSpecificRowsOrColumnsResults.getNewAccessToken());
  
}


//Extrae los valores del objeto xml retornado como respuesta
void parseResults(XML xml_response){
  //println(xml_response);
  //println(xml_response.listChildren());
  
  //Extraemos la lista de entradas de los resultados
  XML[] entries = xml_response.getChildren("entry");
  
  //Iteramos para extraer el contenido
  for(int i = 0; i < entries.length; i++){
    //Obtenemos el objeto xml de cada celda
    XML entry = entries[i].getChild("content");
    //Imprimimos el valor de las celdas
    println(entry.getContent());
  }
}

