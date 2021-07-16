// Country names and ID section

// URL to get dictionary of country codes and country codes
var urlCountry = 'http://127.0.0.1:5000/data/countrylist'
// JSON saved as a variable
fetch(urlCountry)
    .then(response => response.json())
    .then(data => {
        countryNames = data.map(obj => obj.country)
        console.log(countryNames)
        // Displays the currect selection in the dropdownlist
        d3.select("#selDataset")
        .selectAll("myOptions")
            .data(countryNames)
        .enter()
            .append('option')
            // text showed in the menu
        .text(function (d) { return d; })
        // corresponding value returned by the button
        .attr("value", function (d) { return d; })
    })

// Covid data section

// URL to get daily covid data for each country
var urlData = `http://127.0.0.1:5000/data/coviddata`
// JSON saved as a variable
fetch(urlData)
    .then(response => response.json())

