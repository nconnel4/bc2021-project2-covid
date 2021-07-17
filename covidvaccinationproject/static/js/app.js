// COUNTRY NAMES AND ID SECTION

// URL to get dictionary of country codes and country codes
var urlCountry = 'http://127.0.0.1:5000/data/countrylist'
// JSON fetch. File is each country and their corresponding code
fetch(urlCountry)
    .then(response => response.json())
    .then(data => {
        // Variables
        countryNames = data.map(obj => obj.country)
        countryId = data.map(obj => obj.country_id)
        // Displays the currect selection in the dropdownlist
        d3.select("#selDataset")
        .selectAll("myOptions")
            .data(data)
        .enter()
            .append('option')
            // text showed in the menu
        .text(function (d) { return d.country; })
        // corresponding value returned by the button
        .attr("value", function (d) { return d.country_id; })

        // Default metadata for the first option on the list
        var defaultId = document.getElementById("selDataset").value;
        var defaultName = countryNames[countryId.indexOf(defaultId)]; 
        // Enter data into text box
        let ele = document.getElementById("sample-metadata");
        ele.innerHTML += defaultName + "<br />";
        ele.innerHTML += defaultId + "<br />";
    })

// COVID DATA SECTION

// URL to get daily covid data for each country
var urlData = `http://127.0.0.1:5000/data/coviddata`
// JSON fetch. File is of every countries data per day
fetch(urlData)
    .then(response => response.json())
    .then(data => {
        // Variables
        countryIdDaily = data.map(obj => obj.country_id)
        date = data.map(obj => obj.date)
        totalCases = data.map(obj => obj.total_cases)
        totalDeaths = data.map(obj => obj.total_deaths)
        totalVaccinations = data.map(obj => obj.total_vaccinations)
        // Get last index of default ID
        index = countryIdDaily.lastIndexOf(defaultId)
        // Default metadata for current day for the default option on the list
        var defaultCurrentDate = date[index]
        var defaultCurrentCases = totalCases[index]
        var defaultCurrentDeaths = totalDeaths[index]
        var defaultCurrentVaccinations = totalVaccinations[index]
        // Enter data into text box
        let ele = document.getElementById("sample-metadata");
        ele.innerHTML += defaultCurrentDate + "<br />";
        ele.innerHTML += defaultCurrentCases + "<br />";
        ele.innerHTML += defaultCurrentDeaths + "<br />";
        ele.innerHTML += defaultCurrentVaccinations + "<br />";
    })

// COUNTRY SELECTION CHANGED SECTION

// Function to run whenever an option is changed
function optionChanged(value){
    // Delete text in box to create new text
    document.getElementById("sample-metadata").innerHTML = "";
    // Get values of data
    idMatch = value;
    // Match country name to country ID
    nameMatch = countryNames[countryId.indexOf(idMatch)];
    // Enter data into text box
    let ele = document.getElementById("sample-metadata");
    ele.innerHTML += nameMatch + "<br />";
    ele.innerHTML += idMatch + "<br />";
}