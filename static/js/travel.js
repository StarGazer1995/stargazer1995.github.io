(function () {
  if (!window.L) return;

  var TILE = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';

  function makeMap(el, center, zoom) {
    var map = L.map(el, { scrollWheelZoom: false, zoomControl: true });
    map.setView(center || [30, 110], zoom || 4);
    L.tileLayer(TILE, { attribution: ATTR, subdomains: 'abc', maxZoom: 19 }).addTo(map);
    return map;
  }

  function icon(label, kind) {
    return L.divIcon({
      className: 'trip-pin ' + (kind || ''),
      html: '<span>' + label + '</span>',
      iconSize: [34, 34],
      iconAnchor: [17, 17],
      popupAnchor: [0, -18]
    });
  }

  var KIND_LABEL = { flight: '飞机', drive: '自驾', train: '铁路', stay: '住宿', star: '拍星' };

  var trips = window.TRAVEL_TRIPS || [];
  var indexEl = document.getElementById('travel-map');

  if (indexEl && trips.length) {
    var map = makeMap(indexEl, [30, 110], 4);
    var markers = {};
    var bounds = [];

    trips.forEach(function (t) {
      var c = t.center || (t.route && t.route[0] ? [t.route[0].lat, t.route[0].lon] : null);
      if (!c) return;
      var kind = t.status === '已去' ? 'visited' : 'planned';
      var marker = L.marker(c, { icon: icon(t.days || '·', kind) }).addTo(map);
      marker.bindPopup(
        '<strong>' + t.title + '</strong><br>' +
        t.start + ' – ' + t.end + '<br>' +
        '<a href="/travel/' + t.slug + '/">查看行程 →</a>'
      );
      markers[t.slug] = marker;
      bounds.push(c);
    });

    if (bounds.length) map.fitBounds(bounds, { padding: [30, 30] });

    var buttons = document.querySelectorAll('[data-filter]');
    var cards = document.querySelectorAll('.trip-card');

    function matches(t, f) {
      if (f === 'all') return true;
      if (f === 'visited') return t.status === '已去';
      if (f === 'planned') return t.status === '计划中';
      return t.type === f;
    }

    function apply(f) {
      var visible = [];
      buttons.forEach(function (b) {
        b.classList.toggle('active', b.getAttribute('data-filter') === f);
      });
      trips.forEach(function (t) {
        var ok = matches(t, f);
        var card = document.querySelector('.trip-card[data-slug="' + t.slug + '"]');
        if (card) card.hidden = !ok;
        if (markers[t.slug]) {
          if (ok) {
            markers[t.slug].addTo(map);
            var c = markers[t.slug].getLatLng();
            visible.push([c.lat, c.lng]);
          } else {
            map.removeLayer(markers[t.slug]);
          }
        }
      });
      if (visible.length) map.fitBounds(visible, { padding: [30, 30] });
    }

    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        apply(b.getAttribute('data-filter'));
      });
    });

    setTimeout(function () { map.invalidateSize(); }, 200);
  }

  var trip = window.TRIP;
  var detailEl = document.getElementById('trip-map');

  if (detailEl && trip && trip.route) {
    var first = trip.route[0];
    var detailMap = makeMap(detailEl, [first.lat, first.lon], 8);
    var detailBounds = [];

    for (var i = 0; i < trip.route.length - 1; i++) {
      var a = trip.route[i];
      var b = trip.route[i + 1];
      var dashed = a.kind === 'flight' || b.kind === 'flight';
      L.polyline([[a.lat, a.lon], [b.lat, b.lon]], {
        color: '#b85c3e',
        weight: 3,
        opacity: 0.8,
        dashArray: dashed ? '7 9' : null
      }).addTo(detailMap);
    }

    var seen = {};
    trip.route.forEach(function (s) {
      var key = s.name + '|' + s.lat + '|' + s.lon;
      if (seen[key]) return;
      seen[key] = true;
      var label = String(Object.keys(seen).length);
      var marker = L.marker([s.lat, s.lon], { icon: icon(label, s.kind) }).addTo(detailMap);
      marker.bindPopup('<strong>' + s.name + '</strong><br>' + (KIND_LABEL[s.kind] || s.kind || ''));
      detailBounds.push([s.lat, s.lon]);
    });

    if (detailBounds.length) detailMap.fitBounds(detailBounds, { padding: [40, 40] });
    setTimeout(function () { detailMap.invalidateSize(); }, 200);
  }
})();
