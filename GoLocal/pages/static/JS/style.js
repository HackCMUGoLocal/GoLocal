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
          console.log(Http.responseText);
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
async function getAllStores(resolve) {
  // Returns list of stores
  const json = await getRequest("http://127.0.0.1:8000/products/"); // JSON to Products Page
  console.log(json)
  stores = JSON.parse(json);
  resolve(stores);
}

// Returns a parsed list of store dictionaries which have the product given
function getStoresHaving(productName) {
  // Returns list of stores
  const stores = [];
  const json = getRequest("http://127.0.0.1:8000/products/"); // JSON to Products Page
  for(let i = 0; i < json.length; i++) {
    const ithjson = json[i];
    const obj = JSON.parse(ithjson);
    if(obj.name == productName) {
      stores.push(obj.store);
    }
  }
  return stores;
}

// Adds passed in store to store list
function addStore(store) {
  var ul = document.getElementById("store_list");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(store["name"]));
  ul.appendChild(li);
}

function addStores(stores) {
  stores.forEach(store => {
    addStore(store);
  });
}

stores = getAllStores(addStores);
