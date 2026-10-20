(function () {
  if (!window.L) return;

  var TILE = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';

  function makeMap(el, center, zoom) {
    var map = L.map(el, {
      scrollWheelZoom: false,
      zoomControl: true,
      zoomSnap: 0.25,
      zoomDelta: 0.5
    });
    map.setView(center || [30, 110], zoom || 4);
    L.tileLayer(TILE, { attribution: ATTR, subdomains: 'abc', maxZoom: 19 }).addTo(map);

    // macOS trackpad pinch arrives as wheel events with ctrlKey set.
    // Plain two-finger scroll is left alone so the page still scrolls normally.
    var container = map.getContainer();
    map.scrollWheelZoom.disable();
    container.addEventListener('wheel', function (e) {
      if (!e.ctrlKey || map.scrollWheelZoom.enabled()) return;
      e.preventDefault();
      var point = map.mouseEventToContainerPoint(e);
      var next = map.getZoom() - e.deltaY / 120;
      map.setZoomAround(point, Math.max(map.getMinZoom(), Math.min(map.getMaxZoom(), next)));
    }, { passive: false });

    // Clicking the map switches on regular wheel / two-finger scroll zoom.
    container.addEventListener('click', function () {
      if (map.scrollWheelZoom.enabled()) return;
      map.scrollWheelZoom.enable();
      el.classList.add('zoom-active');
      var card = el.closest('.trip-map-card');
      var hint = card && card.querySelector('.map-zoom-hint');
      if (hint) {
        hint.textContent = '滚轮缩放已启用';
        hint.classList.add('is-on');
        setTimeout(function () { hint.classList.add('is-faded'); }, 2200);
      }
    });

    // Safari reports trackpad pinch as gesture events instead of ctrl+wheel.
    var gestureBase = null;
    container.addEventListener('gesturestart', function (e) {
      e.preventDefault();
      gestureBase = map.getZoom();
    });
    container.addEventListener('gesturechange', function (e) {
      e.preventDefault();
      if (gestureBase == null) gestureBase = map.getZoom();
      var point = map.mouseEventToContainerPoint(e);
      map.setZoomAround(point, gestureBase + Math.log2(e.scale || 1));
    });

    el._tripMap = map;
    return map;
  }

  function icon(label, kind, photoCount) {
    return L.divIcon({
      className: 'trip-pin ' + (kind || ''),
      html: '<span>' + label + '</span>' +
        (photoCount ? '<em class="pin-photo-count">📷' + photoCount + '</em>' : ''),
      iconSize: [34, 34],
      iconAnchor: [17, 17],
      popupAnchor: [0, -18]
    });
  }

  function esc(str) {
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/"/g, '&quot;');
  }

  function photoBlock(photos) {
    if (!photos.length) return '';
    var byDay = {};
    photos.forEach(function (p) {
      var key = p.day || '';
      (byDay[key] = byDay[key] || []).push(p);
    });
    var html = '<div class="map-photo-block">' +
      '<p class="map-photo-hint">📷 城市级定位（原片无 GPS）</p>';
    Object.keys(byDay).sort().forEach(function (d) {
      html += '<p class="map-photo-day">' + (d ? d.slice(5) : '日期待补') + '</p>' +
        '<div class="map-photo-grid">';
      byDay[d].forEach(function (p) {
        html += '<a href="' + p.src + '" data-photo data-caption="' + esc(p.caption) + '" title="' + esc(p.caption) + '">' +
          '<img src="' + p.src + '" alt="" loading="lazy"></a>';
      });
      html += '</div>';
    });
    return html + '</div>';
  }

  function photoIcon() {
    return L.divIcon({
      className: 'photo-pin',
      html: '<span>📷</span>',
      iconSize: [30, 30],
      iconAnchor: [15, 15]
    });
  }

  var KIND_LABEL = { flight: '飞机', drive: '自驾', train: '铁路', stay: '住宿', star: '拍星' };

  var trips = window.TRAVEL_TRIPS || [];
  var indexEl = document.getElementById('travel-map');

  if (indexEl && trips.length) {
    var map = makeMap(indexEl, [30, 110], 4);
    var markers = {};
    var photoMarkers = {};
    var bounds = [];

    trips.forEach(function (t) {
      var c = t.center || (t.route && t.route[0] ? [t.route[0].lat, t.route[0].lon] : null);
      if (!c) return;
      var kind = t.status === '已去' ? 'visited' : 'planned';
      var marker = L.marker(c, { icon: icon(t.days || '·', kind) }).addTo(map);
      marker.bindPopup(
        '<strong>' + t.title + '</strong><br>' +
        (t.start && t.end ? t.start + ' – ' + t.end : '日期待补') + '<br>' +
        '<a href="/travel/' + t.slug + '/">查看行程 →</a>'
      );
      markers[t.slug] = marker;
      bounds.push(c);

      (t.gallery || []).forEach(function (p) {
        if (p.lat == null || p.lon == null) return;
        var pm = L.marker([p.lat, p.lon], { icon: photoIcon() }).addTo(map);
        pm.bindPopup(
          '<img src="' + p.src + '" alt="" style="width:180px;border-radius:8px;display:block;margin-bottom:8px">' +
          '<strong>' + p.caption + '</strong>'
        );
        (photoMarkers[t.slug] = photoMarkers[t.slug] || []).push(pm);
      });
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
        (photoMarkers[t.slug] || []).forEach(function (pm) {
          if (ok) pm.addTo(map); else map.removeLayer(pm);
        });
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
    var photoGroups = {};
    var photoPins = [];

    (trip.gallery || []).forEach(function (p) {
      if (!p.place || (p.lat != null && p.lon != null)) return;
      (photoGroups[p.place] = photoGroups[p.place] || []).push(p);
    });

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
      var photos = photoGroups[s.name] || [];
      var marker = L.marker([s.lat, s.lon], { icon: icon(label, s.kind, photos.length) }).addTo(detailMap);
      marker.bindPopup(
        '<strong>' + s.name + '</strong><br>' + (KIND_LABEL[s.kind] || s.kind || '') + photoBlock(photos),
        { maxWidth: 340 }
      );
      detailBounds.push([s.lat, s.lon]);
    });

    (trip.gallery || []).forEach(function (p) {
      if (p.lat == null || p.lon == null) return;
      var pm = L.marker([p.lat, p.lon], { icon: photoIcon() }).addTo(detailMap);
      pm.bindPopup(
        '<img src="' + p.src + '" alt="" style="width:200px;border-radius:8px;display:block;margin-bottom:8px">' +
        '<strong>' + p.caption + '</strong>' + (p.date ? '<br>' + p.date : '')
      );
      detailBounds.push([p.lat, p.lon]);
      photoPins.push(pm);
    });

    if (detailBounds.length) {
      detailMap.fitBounds(detailBounds, {
        paddingTopLeft: [40, 50],
        paddingBottomRight: [40, 110]
      });
    }
    function syncPhotoPins() {
      var show = detailMap.getZoom() >= 9;
      photoPins.forEach(function (pm) {
        if (show) {
          if (!detailMap.hasLayer(pm)) pm.addTo(detailMap);
        } else if (detailMap.hasLayer(pm)) {
          detailMap.removeLayer(pm);
        }
      });
    }
    detailMap.on('zoomend', syncPhotoPins);
    syncPhotoPins();
    setTimeout(function () { detailMap.invalidateSize(); }, 200);
  }

  var lightbox = document.getElementById('photo-lightbox');
  if (lightbox) {
    var lightboxImg = lightbox.querySelector('img');
    var lightboxCap = lightbox.querySelector('p');

    function closeLightbox() {
      lightbox.hidden = true;
      lightboxImg.removeAttribute('src');
      document.body.classList.remove('lightbox-open');
    }

    document.addEventListener('click', function (e) {
      var link = e.target.closest ? e.target.closest('[data-photo]') : null;
      if (!link) return;
      e.preventDefault();
      lightboxImg.src = link.getAttribute('href');
      lightboxCap.textContent = link.getAttribute('data-caption') || '';
      lightbox.hidden = false;
      document.body.classList.add('lightbox-open');
    });

    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox || (e.target.closest && e.target.closest('.photo-lightbox-close'))) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !lightbox.hidden) closeLightbox();
    });
  }
})();
