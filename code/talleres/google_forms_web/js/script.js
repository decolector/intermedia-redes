// Instantiate the client proxy
// You may need to adjust the path to reflect the URI of your server proxy

$(document).ready(function(){

	var img_urls = []; //lista de urls de imagenes y sonidos
	//cargamos el archivo json y guardamos la data en img_urls
	$.get('js/data_test.json', function(data){
		//console.log(data);
		var _data = JSON.stringify(data)
		img_urls = JSON.parse(_data);
		console.log(img_urls);
	});
	var temboo = new TembooProxy('/proxy-server');

	// Add the getValues Choreo
	var getValuesChoreo = temboo.addChoreo('jsGetValues');

	// Add inputs
	getValuesChoreo.setInput('Range', 'respuestas!A2:Q400');
	getValuesChoreo.setInput('SpreadsheetID', '1IHCPpUCUfYd-BpXI6UrUc-t7Bs8Uxan1d6X-MMHKhRk');

	// Esta funcion selecciona todas las respuestas en inserta
	// los videos e imagenes asociados a ellas
	// Usar con cuidado, pues toma mucho tiempo en cargar si hay muchas respuestas
	// en la base de datos

	var showResult = function(outputs, outputFilters) {
		console.log("RRRR");
	    // Display outputs
	    if(outputFilters) {
	    	// Display named output filters
	        for(var name in outputFilters) {
	            //console.log(name + ':');
	            for(var item in outputs[name]) {
	                //console.log('    ' + outputs[name][item]);
	            }
	        }
	    } else {
	    	// Display raw outputs
	        for(var name in outputs) {
	            //console.log(name + ': ' + outputs[name]);
	        }
	    }
			//obrencion de la data que nos interesa
			var results = $.parseJSON(outputs["Response"]);
			var filas = results["values"]; //respuestas
			//iteracion sobre la lista de respuestas
			for(var i = 0; i < filas.length; i++){
				var ul = $("<ul></ul>").appendTo("#results");
				//accedemos a las celdas de la fila
				var fila = filas[i];
				for(var j = 0; j < fila.length ; j++){
					var value = fila[j]; //obtenemos el valor de la celda

					var img_url = null;//aqui guardamos la url de la image o video
					var img_list = img_urls[j];//esta es la lista de urls
					if(img_list != "" && img_list != "undefined"){

					//aqui se define la url de la imagen basados en la respuesta
					if(value == "a" || value.indexOf("a. ") >= 0 ){
							img_url = img_list[0];
						}else if(value == "b" || value.indexOf("b. ") >= 0){
							img_url = img_list[1];
						}else if(value == "c" || value.indexOf("c. ") >= 0){
							img_url = img_list[2];
						}
					}
					//console.log("url: " + img_url);
					//aqui se define si es una imagen de giphy o un video de youtube
					if(img_url){
						if( img_url.indexOf("youtube") !== -1){
								console.log("youtube embed: " + img_url);
								//si es de youtube, insertamos el código de embed
								//que es un <iframe>
								$('#results').append(img_url);
							}else{
								console.log("giphy url: " + img_url );
								//si es de giphy, insertamos un elemento <img>
								$('#results').append('<img src="' + img_url + '">');
							}
						}
					}
				}
			};

	// Esta funcion selecciona un registro de los resultados
	// e inserta los elementos en el elemento #results
	var showResultRandom = function(outputs, outputFilters) {
			// Display outputs
			if(outputFilters) {
				// Display named output filters
					for(var name in outputFilters) {
							//console.log(name + ':');
							for(var item in outputs[name]) {
									//console.log('    ' + outputs[name][item]);
							}
					}
			} else {
				// Display raw outputs
					for(var name in outputs) {
							//console.log(name + ': ' + outputs[name]);
					}
			}
			//obrencion de la data que nos interesa
			var results = $.parseJSON(outputs["Response"]);

			var values = results["values"]; //respuestas

			var index = Math.floor(Math.random() * values.length);
			respuesta = values[index];

			for(var i = 0; i < respuesta.length; i++){
				var img_url = null;
				var value = respuesta[i];
				//console.log(img_urls[i]);
				//si la lista de urls no esta vacia
				if(typeof(img_urls[i]) != "" ){
					//si la respuesta es a
					if(value == "a" || value.indexOf("a. ") >= 0 ){
						  //seleccionamos la primera url de la lista
							img_url = img_urls[i][0];

						}else if(value == "b" || value.indexOf("b. ") >= 0){ // si es b
							img_url = img_urls[i][1]; //seleccionamos la segunda url
						}else if(value == "c" || value.indexOf("c. ") >= 0){ // si es c
							img_url = img_urls[i][2]; //seleccionamos la tercera url
						}
				}
				console.log("url: " + img_url);
				//aca verificamos si la url es de youtube o giphy
				if(img_url){
					if( img_url.indexOf("youtube") !== -1){
							console.log("youtube");
							//si es de youtube es un <iframe>, por lo tanto insertamos el contenido completo
							$('#results').append(img_url);
						}else{
							//si es de giphy, usamos la url como contenido del atributo
							// src del elemento <img>
							console.log("giphy");
							$('#results').append('<img src="' + img_url + '">');
						}
					}
				}
	};


	// Error callback
	var showError = function(error) {
	    if(error.type === 'DisallowedInput') {
	        console.log(error.type + ' error: ' + error.inputName);
	    } else {
	        console.log(error.type + ' error: ' + error.message);
	    }
	};
  //al hacer submit en el boton,
	//se borra el contenido de la division #results
	//y se llama de nuevo a temboo por otros resultados

	$('#load').submit(function(event){
		event.preventDefault();
		$("#results").empty();
		getValuesChoreo.execute(showResultRandom, showError);
	});
	// Run the Choreo, specifying success and error callback handlers

});
