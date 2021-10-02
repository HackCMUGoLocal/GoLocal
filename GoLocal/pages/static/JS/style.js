function getRequest(url) {
  const Http = new XMLHttpRequest();
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
  }
}

getRequest("http://127.0.0.1:8000/products/");

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