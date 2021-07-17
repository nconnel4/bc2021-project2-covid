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

// COUNTRY POPULATION SECTION

// URL to get current population for each country
var urlPopulation = `http://127.0.0.1:5000/data/countrydemo`
// JSON fetch. File is of every countries data per day
fetch(urlPopulation)
    .then(response => response.json())
    .then(data => {
        // Variables
        countryPopulation = data.map(obj => obj.population)
        // countryId = data.map(obj => obj.country_id)
        // Default metadata for the first option on the list
        var defaultId = document.getElementById("selDataset").value;
        var defaultPopulation = countryPopulation[countryId.indexOf(defaultId)]; 
        // Enter data into text box
        let ele = document.getElementById("sample-metadata");
        ele.innerHTML += "Population: " + defaultPopulation + "<br />";
    })

// COVID DATA SECTION

// URL to get daily covid data for each country
var urlData = `http://127.0.0.1:5000/data/coviddata?most_recent=1`
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
        var defaultId = document.getElementById("selDataset").value;
        index = countryIdDaily.lastIndexOf(defaultId)
        // Default metadata for current day for the default option on the list
        var defaultCurrentDate = formatDate(new Date(date[index]))
        var defaultCurrentCases = totalCases[index]
        var defaultCurrentDeaths = totalDeaths[index]
        var defaultCurrentVaccinations = totalVaccinations[index]
        // Turn any null values to 0
        if(defaultCurrentCases == null){
            defaultCurrentCases = 0
        }
        if(defaultCurrentDeaths == null){
            defaultCurrentDeaths = 0
        }
        if(defaultCurrentVaccinations == null){
            defaultCurrentVaccinations = 0
        }
        // Enter data into text box
        let ele = document.getElementById("sample-metadata");
        ele.innerHTML += "Date: " + defaultCurrentDate + "<br />";
        ele.innerHTML += "Covid Cases: " + defaultCurrentCases + "<br />";
        ele.innerHTML += "Total Deaths: " + defaultCurrentDeaths + "<br />";
        ele.innerHTML += "Total Vaccinations: " + defaultCurrentVaccinations + "<br />";
    })

// COUNTRY SELECTION CHANGED SECTION

// Function to run whenever an option is changed
function optionChanged(value){
    // Delete text in box to create new text
    document.getElementById("sample-metadata").innerHTML = "";
    // Get values of data
    currentId = value;
    // Get last index of ID
    var currentId = document.getElementById("selDataset").value;
    index = countryIdDaily.lastIndexOf(currentId)
    // Match country name and population to country ID
    nameMatch = countryNames[countryId.indexOf(currentId)];
    currentPopulation = countryPopulation[countryId.indexOf(currentId)]
    // Metadata for current day for the selected option on the list
    var currentDate = formatDate(new Date(date[index]))
    var currentCases = totalCases[index]
    var currentDeaths = totalDeaths[index]
    var currentVaccinations = totalVaccinations[index]
    // Turn any null values to 0
    if(currentCases == null){
        currentCases = 0
    }
    if(currentDeaths == null){
        currentDeaths = 0
    }
    if(currentVaccinations == null){
        currentVaccinations = 0
    }
    // Enter data into text box
    let ele = document.getElementById("sample-metadata");
    ele.innerHTML += nameMatch + "<br />";
    ele.innerHTML += currentId + "<br />";
    ele.innerHTML += "Population: " + currentPopulation + "<br />";
    ele.innerHTML += "Date: " + currentDate + "<br />";
    ele.innerHTML += "Covid Cases: " + currentCases + "<br />";
    ele.innerHTML += "Total Deaths: " + currentDeaths + "<br />";
    ele.innerHTML += "Total Vaccinations: " + currentVaccinations + "<br />";
}

// Function to format the date into month/day/year
function formatDate(date){
    var year = date.getFullYear()
    var month = (1 + date.getMonth()).toString()
    var day = date.getDate()
    return month + "/" + day + "/" + year
}