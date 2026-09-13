/* InKozi — shared behaviour for auth pages (presentation only) */
(function () {
  'use strict';

  /* Show / hide password */
  document.querySelectorAll('.pw-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var input = btn.parentElement.querySelector('input');
      if (!input) return;
      var show = input.type === 'password';
      input.type = show ? 'text' : 'password';
      btn.innerHTML = show ? '<i class="bi bi-eye-slash"></i>' : '<i class="bi bi-eye"></i>';
      btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
    });
  });

  /* Password strength meter + rule list */
  document.querySelectorAll('[data-strength]').forEach(function (input) {
    var pick = function (attr) {
      var sel = input.getAttribute(attr);
      return sel ? document.querySelector(sel) : null;
    };
    var meter = pick('data-strength');
    var rules = pick('data-rules');
    var confirm = pick('data-confirm');

    function check() {
      var v = input.value || '';
      var tests = {
        len: v.length >= 8,
        upper: /[A-Z]/.test(v),
        num: /\d/.test(v),
        sym: /[^A-Za-z0-9]/.test(v)
      };
      var score = Object.keys(tests).filter(function (k) { return tests[k]; }).length;
      if (meter) meter.setAttribute('data-score', v ? score : 0);
      if (rules) {
        Object.keys(tests).forEach(function (k) {
          var li = rules.querySelector('[data-rule="' + k + '"]');
          if (!li) return;
          li.classList.toggle('ok', tests[k]);
          var icon = li.querySelector('i');
          if (icon) icon.className = tests[k] ? 'bi bi-check-circle-fill' : 'bi bi-circle';
        });
      }
      if (confirm && confirm.value) {
        confirm.classList.toggle('is-invalid', confirm.value !== v);
      }
    }
    input.addEventListener('input', check);
    if (confirm) {
      confirm.addEventListener('input', function () {
        confirm.classList.toggle('is-invalid', confirm.value !== '' && confirm.value !== input.value);
      });
    }
  });

  /* One-time-code inputs: auto advance, backspace, paste */
  document.querySelectorAll('.otp').forEach(function (group) {
    var inputs = Array.prototype.slice.call(group.querySelectorAll('input'));
    inputs.forEach(function (el, i) {
      el.addEventListener('input', function () {
        el.value = el.value.replace(/\D/g, '').slice(-1);
        el.classList.toggle('filled', !!el.value);
        if (el.value && inputs[i + 1]) inputs[i + 1].focus();
      });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Backspace' && !el.value && inputs[i - 1]) {
          inputs[i - 1].focus();
        } else if (e.key === 'ArrowLeft' && inputs[i - 1]) {
          inputs[i - 1].focus();
        } else if (e.key === 'ArrowRight' && inputs[i + 1]) {
          inputs[i + 1].focus();
        }
      });
      el.addEventListener('focus', function () { el.select(); });
      el.addEventListener('paste', function (e) {
        var text = (e.clipboardData || window.clipboardData).getData('text').replace(/\D/g, '');
        if (!text) return;
        e.preventDefault();
        inputs.forEach(function (box, j) {
          box.value = text[j] || '';
          box.classList.toggle('filled', !!box.value);
        });
        (inputs[Math.min(text.length, inputs.length) - 1] || inputs[0]).focus();
      });
    });
  });

  /* Resend countdown */
  document.querySelectorAll('[data-countdown]').forEach(function (btn) {
    var total = parseInt(btn.getAttribute('data-countdown'), 10) || 45;
    var label = btn.getAttribute('data-label') || 'Resend code';
    var left = total;
    function tick() {
      if (left <= 0) {
        btn.disabled = false;
        btn.textContent = label;
        return;
      }
      var m = Math.floor(left / 60), s = left % 60;
      btn.disabled = true;
      btn.textContent = label + ' in ' + m + ':' + (s < 10 ? '0' : '') + s;
      left -= 1;
      setTimeout(tick, 1000);
    }
    btn.addEventListener('click', function () {
      if (btn.disabled) return;
      left = total;
      tick();
    });
    tick();
  });

  /* Dropzone */
  document.querySelectorAll('.dropzone').forEach(function (zone) {
    var input = zone.querySelector('input[type="file"]');
    var name = zone.querySelector('.dz-file span');
    if (!input) return;
    zone.addEventListener('click', function () { input.click(); });
    input.addEventListener('change', function () {
      if (input.files && input.files[0]) {
        zone.classList.add('has-file');
        if (name) name.textContent = input.files[0].name;
      }
    });
    ['dragenter', 'dragover'].forEach(function (ev) {
      zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.add('drag'); });
    });
    ['dragleave', 'drop'].forEach(function (ev) {
      zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.remove('drag'); });
    });
    zone.addEventListener('drop', function (e) {
      if (e.dataTransfer && e.dataTransfer.files[0]) {
        zone.classList.add('has-file');
        if (name) name.textContent = e.dataTransfer.files[0].name;
      }
    });
  });

  /* Segmented switch: move the sliding pill when a tab is shown */
  document.querySelectorAll('.seg').forEach(function (seg) {
    var links = Array.prototype.slice.call(seg.querySelectorAll('.nav-link'));
    links.forEach(function (link, i) {
      if (link.classList.contains('active')) seg.setAttribute('data-active', i);
      link.addEventListener('shown.bs.tab', function () {
        seg.setAttribute('data-active', i);
      });
    });
  });

  /* Copy-to-clipboard helpers (error reference ids) */
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var el = document.querySelector(btn.getAttribute('data-copy'));
      if (!el || !navigator.clipboard) return;
      navigator.clipboard.writeText(el.textContent.trim()).then(function () {
        var was = btn.textContent;
        btn.textContent = 'Copied';
        setTimeout(function () { btn.textContent = was; }, 1600);
      });
    });
  });

  /* Demo forms: do not navigate away when a form has no real action */
  document.querySelectorAll('form[data-next]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.checkValidity()) {
        var target = form.getAttribute('data-next');
        var next = new URLSearchParams(window.location.search).get('next');
        if (next && /^[\w-]+\.html$/.test(next)) {
          if (form.hasAttribute('data-final')) {
            target = next;
          } else {
            target += (target.indexOf('?') > -1 ? '&' : '?') + 'next=' + encodeURIComponent(next);
          }
        }
        window.location.href = target;
      } else {
        form.reportValidity();
      }
    });
  });
})();
