function isValidURL(str) {
    var pattern = new RegExp(
        "^(https?:\\/\\/)?" + // protocol
        "((([a-zA-Z0-9$_.+!*',;?&=-]|%[0-9a-fA-F]{2})+(:([a-zA-Z0-9$_.+!*',;?&=-]|%[0-9a-fA-F]{2})+)?@)?" + // user:pass
        "((([a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9])|([a-zA-Z0-9]))\\.)+([a-zA-Z]{2,6})|" + // domain name
        "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
        "(\\:\\d+)?(\\/[-a-zA-Z0-9%_.~+]*)*" + // port and path
        "(\\?[;&a-zA-Z0-9%_.~+=-]*)?" + // query string
        "(\\#[-a-zA-Z0-9_]*)?$",
        "i"
    ); // fragment locator
    return !!pattern.test(str);
}

function send_input() {
    event.preventDefault();
    const input = document.getElementById("input_field").value;
    console.log("Searching for:", input);
    fetch("/request_search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            value: document.getElementById("input_field").value,
        }),
    })
        .then((response) => response.json())
        .then((response) => displayResults(response));
}

function displayResults(data) {
    const resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = ""; // Clear previous results

    // Create table
    const table = document.createElement("table");

    // Create table headers
    const headerRow = document.createElement("tr");
    Object.keys(data[0]).forEach((key) => {
        const th = document.createElement("th");
        th.innerText = key;
        headerRow.appendChild(th);
    });
    table.appendChild(headerRow);

    // Create table rows
    Object.values(data).forEach((item) => {
        const row = document.createElement("tr");
        Object.values(item).forEach((value) => {
            const td = document.createElement("td");
            td.innerText = value;

            row.appendChild(td);
        });
        table.appendChild(row);
    });

    resultsContainer.appendChild(table);
}

function send_input() {
    event.preventDefault();
    const input = document.getElementById("input_field").value;
    console.log("Searching for:", input);
    fetch("/request_search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            value: document.getElementById("input_field").value,
        }),
    })
        .then((response) => response.json())
        .then((response) => displayResults(response));
}

function checkIfEmailInString(text) {
    var re = /(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;
    return re.test(text);
}

function displayResults(data) {
    const resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = ""; // Clear previous results

    // Create table
    const table = document.createElement("table");

    // Create table headers
    const headerRow = document.createElement("tr");
    Object.keys(data[0]).forEach((key) => {
        const th = document.createElement("th");
        th.innerText = key;
        headerRow.appendChild(th);
    });
    table.appendChild(headerRow);

    // Create table rows
    Object.values(data).forEach((item) => {
        const row = document.createElement("tr");
        Object.values(item).forEach((value) => {
            const td = document.createElement("td");
            if (isValidURL(value)) {
                const a = document.createElement('a')
                url = value.toLowerCase()
                if (checkIfEmailInString(url)) {
                    url = 'mailto:' + url
                } else if (!/^https?:\/\//i.test(url)) {
                    url = 'https://' + url;
                }
                a.href = url
                a.innerText = value
                a.target = '_blank'
                td.appendChild(a)
            } else {
                td.innerText = value;
            }
            row.appendChild(td);
        });
        table.appendChild(row);
    });

    resultsContainer.appendChild(table);
}