
window.onload=function() {
	// var js_data = document.getElementById('dataid').getAttribute('d');
	var js_data = '{{ context }}';
	console.log(js_data)
	console.log("123")
	populateData(js_data)
}

function populateData(packJson) {
	var cnt = 0;
	console.log(packJson.length)
	for(var i = 0; i < packJson.length; i++){
		// console.log(packJson[i])
		cnt++;
		$("#ranking > tbody").append("<tr></tr>");
		$("#ranking tr:last").append("<td>" + cnt + "</td>");
		$("#ranking tr:last").append("<td>" + packJson[i].username + "</td>");
		$("#ranking tr:last").append("<td>" + packJson[i].wrong_moves + "</td>");
	}

}

function loadCovidData(cnt) {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function () {
		if (this.readyState == 4 && this.status == 200) {
			var jsonresult = JSON.parse(this.responseText)
			//pass json result to populate into the table
			populateData(jsonresult);
		}
	};
	xmlhttp.open("GET", "https://coronavirus-tracker-api.herokuapp.com/v2/locations", true);
	xmlhttp.setRequestHeader("Content-Type", "application/json");
	xmlhttp.send();
}
