/* InKozi Admin — shared behaviour (presentation only) */
(function () {
  'use strict';

  /* Sidebar (off-canvas below 1200px) */
  var body = document.body;
  document.querySelectorAll('[data-sb-toggle]').forEach(function (b) {
    b.addEventListener('click', function () { body.classList.toggle('sb-open'); });
  });
  document.querySelectorAll('[data-sb-close]').forEach(function (b) {
    b.addEventListener('click', function () { body.classList.remove('sb-open'); });
  });

  /* Cmd/Ctrl+K focuses the global search */
  document.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      var s = document.querySelector('.tb-search input');
      if (s) { e.preventDefault(); s.focus(); s.select(); }
    }
  });

  /* Select-all checkboxes in tables */
  document.querySelectorAll('[data-check-all]').forEach(function (master) {
    var table = master.closest('table');
    master.addEventListener('change', function () {
      table.querySelectorAll('tbody input[type="checkbox"]').forEach(function (c) { c.checked = master.checked; });
    });
  });

  /* Tooltips */
  if (window.bootstrap) {
    document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(function (el) { new bootstrap.Tooltip(el); });
  }

  /* Password toggle */
  document.querySelectorAll('.pw-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var input = btn.parentElement.querySelector('input');
      var show = input.type === 'password';
      input.type = show ? 'text' : 'password';
      btn.innerHTML = show ? '<i class="bi bi-eye-slash"></i>' : '<i class="bi bi-eye"></i>';
    });
  });

  /* OTP boxes */
  document.querySelectorAll('.otp').forEach(function (group) {
    var inputs = Array.prototype.slice.call(group.querySelectorAll('input'));
    inputs.forEach(function (el, i) {
      el.addEventListener('input', function () {
        el.value = el.value.replace(/\D/g, '').slice(-1);
        if (el.value && inputs[i + 1]) inputs[i + 1].focus();
      });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Backspace' && !el.value && inputs[i - 1]) inputs[i - 1].focus();
      });
    });
  });

  /* Demo toasts for buttons marked data-toast */
  var stack;
  function toast(msg) {
    if (!stack) { stack = document.createElement('div'); stack.className = 'toast-stack'; document.body.appendChild(stack); }
    var t = document.createElement('div');
    t.className = 'toastx';
    t.innerHTML = '<i class="bi bi-check-circle-fill"></i><span></span>';
    t.querySelector('span').textContent = msg;
    stack.appendChild(t);
    setTimeout(function () { t.remove(); }, 2600);
  }
  document.querySelectorAll('[data-toast]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      if (b.tagName === 'A' && b.getAttribute('href') === '#') e.preventDefault();
      toast(b.getAttribute('data-toast'));
    });
  });
  document.querySelectorAll('form[data-demo]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var next = f.getAttribute('data-demo');
      if (next) window.location.href = next; else toast('Saved');
    });
  });

  /* Charts */
  if (!window.Chart) return;
  Chart.defaults.font.family = "'Inter', sans-serif";
  Chart.defaults.font.size = 12;
  Chart.defaults.color = '#94A3B8';
  Chart.defaults.plugins.legend.display = false;
  Chart.defaults.plugins.tooltip.backgroundColor = '#0F172A';
  Chart.defaults.plugins.tooltip.padding = 10;
  Chart.defaults.plugins.tooltip.cornerRadius = 8;
  Chart.defaults.plugins.tooltip.titleFont = { weight: '600' };

  var PINK = '#E00A70', PURPLE = '#8c1fa9', INDIGO = '#4a2bd6', MAG = '#d91d75';
  var grid = { color: 'rgba(15,23,42,0.06)', drawBorder: false };
  var days = function (n) { var a = []; for (var i = n - 1; i >= 0; i--) { var d = new Date(2026, 8, 14); d.setDate(d.getDate() - i); a.push(d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })); } return a; };
  var months = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'];

  function gradientFill(ctx, color) {
    var g = ctx.createLinearGradient(0, 0, 0, 300);
    g.addColorStop(0, color.replace(')', ',0.28)').replace('rgb', 'rgba'));
    g.addColorStop(1, color.replace(')', ',0)').replace('rgb', 'rgba'));
    return g;
  }

  function lineChart(id, labels, sets) {
    var el = document.getElementById(id); if (!el) return;
    var ctx = el.getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: { labels: labels, datasets: sets.map(function (s) {
        return { label: s.label, data: s.data, borderColor: s.color, backgroundColor: gradientFill(ctx, s.rgb), fill: true, tension: 0.4, borderWidth: 2.5, pointRadius: 0, pointHoverRadius: 5, pointHoverBackgroundColor: s.color, pointHoverBorderColor: '#fff', pointHoverBorderWidth: 2 };
      }) },
      options: { responsive: true, maintainAspectRatio: false, interaction: { mode: 'index', intersect: false },
        scales: { x: { grid: { display: false }, ticks: { maxTicksLimit: 8 } }, y: { grid: grid, border: { display: false }, ticks: { maxTicksLimit: 5 }, beginAtZero: true } } }
    });
  }

  function barChart(id, labels, sets, stacked) {
    var el = document.getElementById(id); if (!el) return;
    new Chart(el.getContext('2d'), {
      type: 'bar',
      data: { labels: labels, datasets: sets.map(function (s) { return { label: s.label, data: s.data, backgroundColor: s.color, borderRadius: 6, borderSkipped: false, maxBarThickness: 28 }; }) },
      options: { responsive: true, maintainAspectRatio: false,
        scales: { x: { stacked: !!stacked, grid: { display: false } }, y: { stacked: !!stacked, grid: grid, border: { display: false }, ticks: { maxTicksLimit: 5 }, beginAtZero: true } } }
    });
  }

  function doughnut(id, labels, data, colors) {
    var el = document.getElementById(id); if (!el) return;
    new Chart(el.getContext('2d'), {
      type: 'doughnut',
      data: { labels: labels, datasets: [{ data: data, backgroundColor: colors, borderWidth: 0, hoverOffset: 6 }] },
      options: { responsive: true, maintainAspectRatio: false, cutout: '72%' }
    });
  }

  function series(base, n, amp, seed) {
    var a = [], v = base; for (var i = 0; i < n; i++) { v = Math.max(0, v + Math.sin(i * 0.9 + seed) * amp + ((i * 7919 + seed * 13) % 11 - 5) * (amp / 8) + amp / 12); a.push(Math.round(v)); } return a;
  }

  lineChart('chart-inquiries', days(30), [
    { label: 'Questions asked', data: series(38, 30, 9, 1), color: PINK, rgb: 'rgb(224,10,112)' },
    { label: 'Answered', data: series(31, 30, 8, 2), color: INDIGO, rgb: 'rgb(74,43,214)' }
  ]);
  barChart('chart-revenue', months, [
    { label: 'Subscriptions', data: [48, 52, 55, 61, 66, 70, 74, 79, 83, 88, 92, 97].map(function (v) { return v * 45 * 10 / 1000; }), color: PURPLE },
    { label: 'Set-up fees', data: [6, 4, 5, 7, 6, 8, 5, 9, 6, 8, 7, 9].map(function (v) { return v * 375 / 1000; }), color: '#F9A8D4' }
  ], true);
  doughnut('chart-areas', ['DUI / DWI', 'Family Law', 'Criminal Defense', 'Personal Injury', 'Immigration', 'Other'], [26, 22, 18, 14, 11, 9], [PINK, MAG, PURPLE, INDIGO, '#A78BFA', '#E2E8F0']);
  lineChart('chart-growth', months, [
    { label: 'Users', data: [820, 940, 1080, 1210, 1390, 1560, 1760, 1980, 2210, 2470, 2720, 2980], color: PINK, rgb: 'rgb(224,10,112)' },
    { label: 'Providers', data: [310, 340, 372, 401, 438, 470, 512, 548, 590, 631, 668, 702], color: INDIGO, rgb: 'rgb(74,43,214)' }
  ]);
  barChart('chart-funnel', ['Visited', 'Asked a question', 'Got a reply', 'Connected', 'Retained'], [
    { label: 'People', data: [12400, 3120, 2810, 1470, 618], color: PURPLE }
  ]);
  barChart('chart-territory', ['Orlando', 'Miami', 'Tampa', 'Jacksonville', 'Ft. Lauderdale', 'Tallahassee', 'St. Pete'], [
    { label: 'Filled', data: [5, 6, 4, 6, 7, 1, 3], color: PURPLE },
    { label: 'Open', data: [2, 1, 3, 1, 0, 6, 4], color: '#E2E8F0' }
  ], true);
  lineChart('chart-response', days(14), [
    { label: 'Median first reply (min)', data: [22, 19, 21, 18, 17, 20, 16, 15, 18, 14, 16, 15, 13, 14], color: INDIGO, rgb: 'rgb(74,43,214)' }
  ]);
  barChart('chart-tickets', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], [
    { label: 'Opened', data: [14, 18, 11, 16, 20, 7, 5], color: PINK },
    { label: 'Resolved', data: [12, 15, 14, 13, 19, 9, 6], color: '#CBD5E1' }
  ]);
  doughnut('chart-plans', ['Standard $45', 'Premium $95', 'Trial'], [61, 27, 12], [PURPLE, PINK, '#E2E8F0']);
})();
