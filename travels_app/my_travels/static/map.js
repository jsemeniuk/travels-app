const copy =
    "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 5 });
map.locate()
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([0, 0], 5));

async function load_places() {
    const places_url = `/api/my_travels/?in_bbox=${map
        .getBounds()
        .toBBoxString()}`;
    const response = await fetch(places_url);
    const geojson = await response.json();
    return geojson;
}

async function render_places() {
    const markers = await load_places();
    L.geoJSON(markers)
        .bindPopup((layer) => "<h3>" + layer.feature.properties.name + "</h3>" + "<p><a href='" + layer.feature.id + "'>View more</a></p>")
        .addTo(map);
}

function click_on_map(point) {
    var url= "/new&location=" + point.latlng.lat + "," + point.latlng.lng; 
    window.location = url; 
}


map.on("moveend", render_places);
map.on("click", click_on_map);