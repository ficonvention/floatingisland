(function () {
  'use strict';

  var root = document.querySelector('[data-self-quote]');
  if (!root) return;

  var ko = document.documentElement.lang === 'ko';
  var won = new Intl.NumberFormat('ko-KR');
  // 단가 출처: 회사 기업행사 견적 양식(FIC·Anniversary·Marina Park).
  // 갤러리는 최근 기업행사 견적의 별도 대관·시설 사용 기준을 적용한다.
  var venues = {
    convention: { nameKo: '2F 컨벤션홀', nameEn: '2F Convention Hall', base: 20000000, facility: 3000000, tiers: [[40000000, 0], [30000000, 5000000], [20000000, 10000000]] },
    villa: { nameKo: '2F 빌라 드 노체', nameEn: '2F Villa de Noche', base: 7000000, facility: 1000000, tiers: [[20000000, 0], [10000000, 5000000]] },
    vista: { nameKo: '3F 비스타', nameEn: '3F Vista', base: 15000000, facility: 2000000, tiers: [[20000000, 0], [12000000, 5000000]] },
    terrace: { nameKo: '3F 테라스룸', nameEn: '3F Terrace Room', base: 1500000, facility: 0, tiers: [[3000000, 0]] },
    rive: { nameKo: '3F 리브 고쉬', nameEn: '3F Rive Gauche', base: 5000000, facility: 2000000, tiers: [[10000000, 0]] },
    orchid: { nameKo: '3F 오키드룸', nameEn: '3F Orchid Room', base: 5000000, facility: 2000000, tiers: [[10000000, 0]] },
    rooftop: { nameKo: '4층 루프탑', nameEn: '4F Rooftop', base: 15000000, facility: 2000000, tiers: [[30000000, 0]] },
    anniversary: { nameKo: '애니버셔리', nameEn: 'Anniversary', base: 15000000, facility: 1500000, tiers: [[20000000, 0], [15000000, 5000000]] },
    marina: { nameKo: '마리나파크', nameEn: 'Marina Park', base: 15000000, facility: 1500000, tiers: [[20000000, 0], [15000000, 5000000]] },
    gallery: { nameKo: '갤러리', nameEn: 'Gallery', base: 2000000, facility: 1000000, tiers: [] }
  };

  var typeButtons = root.querySelectorAll('[data-quote-type]');
  var panels = root.querySelectorAll('[data-quote-panel]');
  var weddingFrame = root.querySelector('[data-wedding-frame]');

  function chooseType(type, updateUrl) {
    typeButtons.forEach(function (button) {
      var active = button.getAttribute('data-quote-type') === type;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
    panels.forEach(function (panel) {
      panel.hidden = panel.getAttribute('data-quote-panel') !== type;
    });
    if (type === 'wedding' && weddingFrame && !weddingFrame.src) {
      weddingFrame.src = weddingFrame.getAttribute('data-src');
    }
    if (updateUrl && history.replaceState) {
      history.replaceState(null, '', location.pathname + '?type=' + type);
    }
    var activePanel = root.querySelector('[data-quote-panel="' + type + '"]');
    if (activePanel) activePanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  typeButtons.forEach(function (button) {
    button.addEventListener('click', function () { chooseType(button.getAttribute('data-quote-type'), true); });
  });

  var form = root.querySelector('[data-corporate-form]');
  var result = root.querySelector('[data-corporate-result]');
  if (form && result) {
    var venueSelect = form.elements.venue;
    Object.keys(venues).forEach(function (key) {
      var item = venues[key];
      var option = document.createElement('option');
      option.value = key;
      option.textContent = ko ? item.nameKo : item.nameEn;
      venueSelect.appendChild(option);
    });

    function money(value) { return won.format(Math.round(value)) + (ko ? '원' : ' KRW'); }
    function row(label, value, detail) {
      return '<div class="estimate-row"><span>' + label + (detail ? '<small>' + detail + '</small>' : '') + '</span><strong>' + money(value) + '</strong></div>';
    }
    function calculate() {
      var venue = venues[venueSelect.value] || venues.convention;
      var guests = Math.max(10, parseInt(form.elements.guests.value, 10) || 10);
      var meal = parseInt(form.elements.meal.value, 10) || 0;
      var beverage = parseInt(form.elements.beverage.value, 10) || 0;
      var food = guests * (meal + beverage);
      var venueFee = venue.base;
      var waiver = '';
      venue.tiers.some(function (tier) {
        if (food >= tier[0]) {
          venueFee = tier[1];
          waiver = ko ? '식음료 금액 기준 할인 적용' : 'F&B threshold discount applied';
          return true;
        }
        return false;
      });
      var flower = form.elements.flower.checked ? 1000000 : 0;
      var tableQty = Math.max(0, parseInt(form.elements.tableQty.value, 10) || 0);
      var tableUnit = parseInt(form.elements.tableFlower.value, 10) || 0;
      var tableFlower = tableQty * tableUnit;
      var bannerQty = Math.max(0, parseInt(form.elements.bannerQty.value, 10) || 0);
      var banner = bannerQty * 30000;
      var options = flower + tableFlower + banner;
      var subtotal = food + venueFee + venue.facility + options;
      var vat = Math.round(subtotal * 0.1);
      var total = subtotal + vat;
      form.querySelector('[data-rental-display]').textContent = money(venueFee) + (waiver ? ' · ' + waiver : '');
      form.querySelector('[data-facility-display]').textContent = money(venue.facility);
      result.innerHTML =
        '<h3>' + (ko ? '기업행사 예상 견적' : 'Corporate event estimate') + '</h3>' +
        '<p class="estimate-meta">' + (ko ? '행사 시작' : 'Event starts') + ': ' + (form.elements.eventDate.value || (ko ? '날짜 미정' : 'date TBD')) + ' ' + (form.elements.eventTime.value || '') + '</p>' +
        row(ko ? '식음료' : 'Food & beverage', food, money(meal + beverage) + ' × ' + guests) +
        row(ko ? '대관료' : 'Venue rental', venueFee, waiver) +
        row(ko ? '시설 사용료' : 'Facility fee', venue.facility, '') +
        (options ? row(ko ? '선택 옵션' : 'Options', options, '') : '') +
        '<div class="estimate-row estimate-sub"><span>' + (ko ? '소계' : 'Subtotal') + '</span><strong>' + money(subtotal) + '</strong></div>' +
        '<div class="estimate-row"><span>' + (ko ? '부가세 10%' : 'VAT 10%') + '</span><strong>' + money(vat) + '</strong></div>' +
        '<div class="estimate-row estimate-total"><span>' + (ko ? '예상 합계' : 'Estimated total') + '</span><strong>' + money(total) + '</strong></div>';
    }
    form.addEventListener('input', calculate);
    form.addEventListener('change', calculate);
    calculate();
  }

  var requested = new URLSearchParams(location.search).get('type');
  if (requested === 'corporate' || requested === 'wedding') chooseType(requested, false);
})();
