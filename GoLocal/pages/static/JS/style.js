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
}