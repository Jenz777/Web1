/* Tự thêm dấu chấm ngăn cách hàng nghìn khi gõ vào ô khoảng giá (1000 -> 1.000, 1234567 -> 1.234.567).
   Chỉ định dạng hiển thị trong ô nhập; không kiểm tra, không lưu hay đọc dữ liệu nào. */
(function () {
  function format(el) {
    var before = el.value.slice(0, el.selectionStart || 0).replace(/\D/g, '').length;
    var digits = el.value.replace(/\D/g, '');
    el.value = digits.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    var pos = 0, seen = 0;
    while (pos < el.value.length && seen < before) { if (/\d/.test(el.value.charAt(pos))) seen++; pos++; }
    if (el.setSelectionRange) el.setSelectionRange(pos, pos);
  }
  var inputs = document.querySelectorAll('input[data-gia]');
  for (var i = 0; i < inputs.length; i++) inputs[i].addEventListener('input', function () { format(this); });
})();
