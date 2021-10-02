// Return json string from given url
async function getRequest(url) {
  resolve = (responseText) => responseText;

  requestPromise = new Promise((resolve, reject) => {
    const Http = new XMLHttpRequest();
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
      // In local files, status is 0 upon success in Mozilla Firefox
      if(Http.readyState === XMLHttpRequest.DONE) {
        var status = Http.status;
        if (status === 0 || (status >= 200 && status < 400)) {
          // The request has been completed successfully
          resolve(Http.responseText);
        } else {
          // Oh no! There has been an error with the request!
          reject();
        }
      }
    }
  });

  return requestPromise
}

// Return json string from given url
async function postRequest(url, body) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url, false);

  xhr.onreadystatechange = function() { // Call a function when the state changes.
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
          // Request finished. Do processing here.
      }
  }

  resolve = (responseText) => responseText;

  requestPromise = new Promise((resolve, reject) => {
    const Http = new XMLHttpRequest();
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
      // In local files, status is 0 upon success in Mozilla Firefox
      if(Http.readyState === XMLHttpRequest.DONE) {
        var status = Http.status;
        if (status === 0 || (status >= 200 && status < 400)) {
          // The request has been completed successfully
          resolve(Http.responseText);
        } else {
          // Oh no! There has been an error with the request!
          reject();
        }
      }
    }
  });

  return requestPromise
}

// Returns a parsed list of store dictionaries
async function getAllStores() {
  // Returns list of stores
  const json = await getRequest("http://127.0.0.1:8000/stores/"); // JSON to Products Page
  stores = JSON.parse(json);
  return stores;
}

async function getStoresWithID(id) {
  const json = await getRequest("http://127.0.0.1:8000/stores/" + id);
  stores = JSON.parse(json);
  return stores;
}

async function getStoresWithCategory(category) {
  stores = getAllStores();
  stores = stores.filter(store => store['categry']==category);
  return stores;
}

// Adds passed in store to store list
function addStore(store) {
  var ul = document.getElementById("store_list");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(store["name"]));
  ul.appendChild(li);
}

function createTile(name, address, website) {

  const li = document.createElement("li");
  li.className = "store";
  const header = document.createElement("h2");
  li.appendChild(header);
  const headerText = document.createTextNode(name + " | " + address + " | " + website);
  header.appendChild(headerText);

  return li;
}

function addTile(tile) {
  store_list = document.getElementById("store_list");
  store_list.appendChild(tile);
}

function addStores(stores) {
  stores.forEach(store => {
    tile = createTile(store['name'], store['address'], store['website']);
    addTile(tile);
  });
}

function setStores(stores) {
  var ul = document.getElementById("store_list");
  while (ul.firstChild) {
    ul.removeChild(ul.firstChild);
  }
  addStores(stores);
}

async function defaultStores() {
  stores = await getAllStores();
  setStores(stores);
}

defaultStores();