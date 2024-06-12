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

function send_input(event) {
  event.preventDefault();
  const input = document.getElementById('input_field').value;
  const button = document.getElementById('submit_input');
  const loader = document.getElementById('loader');
  loader.style.display = "block";
  button.style.display = "none";
  fetch('/request_search', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      value: document.getElementById('input_field').value,
      country_code: document.getElementById('country_code_dropdown').value
    }),
  })
    .then((response) => response.json())
    .then((response) => displayResults(response));
}

/*function send_input() {
  event.preventDefault();
  const input = document.getElementById('input_field').value;
  console.log('Searching for:', input);
  fetch('/request_search', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      value: document.getElementById('input_field').value,
      country_code: document.getElementById('country_code_dropdown').value
    }),
  })
    .then((response) => response.json())
    .then((response) => displayResults(response));
}*/

function checkIfEmailInString(text) {
  var re =
    /(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;
  return re.test(text);
}

function displayResults(data) {
  const button = document.getElementById('submit_input');
  const loader = document.getElementById('loader');
  loader.style.display = "none";
  const resultsContainer = document.getElementById('results');
  resultsContainer.innerHTML = '';  // Clear previous results
  button.style.display = "block";

  // Define the order of keys
  const keysOrder = [
    '',  // New column for checkbox
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
  table.id = 'table_result'

  // Create table headers
  const headerRow = document.createElement('tr');
  keysOrder.forEach((key) => {
    const th = document.createElement('th');
    th.innerText = key;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  // Create table rows
  dataArray.forEach((item, index) => {
    const row = document.createElement('tr');

    // Create checkbox cell
    const checkboxCell = document.createElement('td');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.class = 'checkbox_export'
    checkbox.id = `checkbox_${index}`;
    checkboxCell.appendChild(checkbox);
    row.appendChild(checkboxCell);

    // Create data cells
    keysOrder.slice(1).forEach((key) => {
      // Skip the first 'Checkbox' key
      const td = document.createElement('td');
      if (key === 'Checkbox') {
        // Skip as checkbox is already added
      } else if (isValidURL(item[key])) {
        const a = document.createElement('a');
        let url = item[key].toLowerCase();
        if (checkIfEmailInString(url)) {
          url = 'mailto:' + url;
        } else if (!/^https?:\/\//i.test(url)) {
          url = 'https://' + url;
        }
        a.href = url;
        a.innerText = item[key];
        a.target = '_blank';
        td.appendChild(a);
      } else {
        td.innerText = item[key];
      }
      row.appendChild(td);
    });

    table.appendChild(row);
  });

  resultsContainer.appendChild(table);
}

function exportJson() {
  var object = {}
  var obj_lst = []
  var list = document.getElementsByClassName('checkbox_export')

  var table = document.getElementById("table_result");
  for (var i = 1, row; row = table.rows[i]; i++) {
    for (var j = 1, col; col = row.cells[j]; j++) {
      const checkbox = row.querySelector('input[type="checkbox"]');
      if (checkbox && checkbox.checked) {
        object[table.rows[0].cells[j].innerText] = col.innerText
      }
    }
    if (Object.keys(object).length != 0) {
      obj_lst.push(object)
    }
    object = {}
  }
  if (obj_lst.length == 0) {
    alert("Please select at least 1 element")
  } else {
    var json = JSON.stringify(obj_lst)
    let jsonContent = "data:text/json;charset=utf-8," + encodeURIComponent(json);
    const link = document.createElement("a");
    link.setAttribute("href", jsonContent);
    link.setAttribute("download", "export.json");
    link.click();
  }
}

function exportCheckedRows() {
  const rows = document.querySelectorAll('#results table tr');
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

  let csvContent = 'data:text/csv;charset=utf-8,';
  csvContent += keysOrder.join(',') + '\n';

  rows.forEach((row, index) => {
    if (index === 0) return;
    const checkbox = row.querySelector('input[type="checkbox"]');
    if (checkbox && checkbox.checked) {
      const cells = row.querySelectorAll('td');
      const rowContent = [];
      cells.forEach((cell, cellIndex) => {
        if (cellIndex === 0) return;
        rowContent.push(cell.innerText);
      });
      csvContent += rowContent.join(',') + '\n';
    }
  });
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0');
  var yyyy = today.getFullYear();
  link.setAttribute(
      'download',
      `supplier_search_${document.getElementById('input_field').value}_${dd}_${mm}_${yyyy}.csv`);
  document.body.appendChild(link);
  if (csvContent.length != 117)
    link.click();
  else
    alert("Please select a row to export");
  document.body.removeChild(link);
}
