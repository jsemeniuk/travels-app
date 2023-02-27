const copy =
    "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 5 });
map.locate()
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([0, 0], 5));

L.geolet({ position: 'topleft' }).addTo(map);

async function load_places() {
    const places_url = `/api/visited_places/?in_bbox=${map
        .getBounds()
        .toBBoxString()}`;
    const response = await fetch(places_url);
    const geojson = await response.json();
    return geojson;
}

async function load_wishlist() {
    const wishlist_url = `/api/wishlist/?in_bbox=${map
        .getBounds()
        .toBBoxString()}`;
    const response = await fetch(wishlist_url);
    const geojson = await response.json();
    return geojson;
}

function wishlistIcon (feature, latlng) {
    let myIcon = L.icon({
      iconUrl: 'static/images/pink-marker-icon.png',
      shadowUrl: 'static/images/marker-shadow.png',
      iconAnchor:   [12, 41], 
      popupAnchor:  [0, -41]
    })
    return L.marker(latlng, { icon: myIcon })
  }
  
  let myLayerOptions = {
    pointToLayer: wishlistIcon
  }

async function render() {
    const places_markers = await load_places();
    L.geoJSON(places_markers)
        .bindPopup((layer) => "<h3>" + layer.feature.properties.name + "</h3>" + "<p><a href='" + layer.feature.id + "'>View more</a></p>")
        .addTo(map);
    const wishlist_markers = await load_wishlist();
    L.geoJSON(wishlist_markers, myLayerOptions)
        .bindPopup((layer) => "<h3>" + layer.feature.properties.name + "</h3>" + "<p><a href='" + layer.feature.id + "'>View more</a></p>")
        .addTo(map);
}

function click_on_map(point) {
    var url= "/new/location=" + point.latlng.lat + "," + point.latlng.lng; 
    window.location = url; 
}

map.on("moveend", render);
map.on("click", click_on_map);


