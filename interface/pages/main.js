function isValidURL(str) {
  var pattern = new RegExp(
      '^(https?:\\/\\/)?' +  // protocol
          '((([a-zA-Z0-9$_.+!*\',;?&=-]|%[0-9a-fA-F]{2})+(:([a-zA-Z0-9$_.+!*\',;?&=-]|%[0-9a-fA-F]{2})+)?@)?' +  // user:pass
          '((([a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9])|([a-zA-Z0-9]))\\.)+([a-zA-Z]{2,6})|' +  // domain name
          '((\\d{1,3}\\.){3}\\d{1,3}))' +         // OR ip (v4) address
          '(\\:\\d+)?(\\/[-a-zA-Z0-9%_.~+]*)*' +  // port and path
          '(\\?[;&a-zA-Z0-9%_.~+=-]*)?' +         // query string
          '(\\#[-a-zA-Z0-9_]*)?$',
      'i');  // fragment locator
  return !!pattern.test(str);
}

function send_input() {
  event.preventDefault();
  const input = document.getElementById('input_field').value;
  console.log('Searching for:', input);
  fetch('/request_search', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      value: document.getElementById('input_field').value,
    }),
  })
      .then((response) => response.json())
      .then((response) => displayResults(response));
}

function send_input() {
  event.preventDefault();
  const input = document.getElementById('input_field').value;
  console.log('Searching for:', input);
  fetch('/request_search', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      value: document.getElementById('input_field').value,
      country_code: document.getElementById("country_code_dropdown").value
    }),
  })
      .then((response) => response.json())
      .then((response) => displayResults(response));
}

function checkIfEmailInString(text) {
  var re =
      /(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;
  return re.test(text);
}

function displayResults(data) {
  const resultsContainer = document.getElementById('results');
  resultsContainer.innerHTML = '';  // Clear previous results

  // Define the order of keys
  const keysOrder = [
    'Name',
    'Location',
    'Link',
    'Contact',
    'Revenue',
    'Size',
    'Certifications',
    'Skills',
    'Main domain',
    'Main customers',
  ];

  // Convert data object to array of objects
  const dataArray = Object.values(data);

  // Create table
  const table = document.createElement('table');

  // Create table headers
  const headerRow = document.createElement('tr');
  keysOrder.forEach((key) => {
    const th = document.createElement('th');
    th.innerText = key;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  // Create table rows
  dataArray.forEach((item) => {
    const row = document.createElement('tr');
    keysOrder.forEach((key) => {
      const td = document.createElement('td');
      if (isValidURL(item[key])) {
        const a = document.createElement('a')
        url = item[key].toLowerCase()
        if (checkIfEmailInString(url)) {
          url = 'mailto:' + url
        }
        else if (!/^https?:\/\//i.test(url)) {
          url = 'https://' + url;
        }
        a.href = url
        a.innerText = item[key]
        a.target = '_blank'
        td.appendChild(a)
      } else {
        td.innerText = item[key];
      }
      row.appendChild(td);
    });
    table.appendChild(row);
  });

  resultsContainer.appendChild(table);
}
