/* Xem trước ảnh sản phẩm ngay khi chọn file (đây là đoạn JavaScript duy nhất của khu vực admin; không lưu/đọc dữ liệu nào). */
(function () {
  var input = document.getElementById('pimg'), img = document.getElementById('pimgv'),
      ph = document.getElementById('pph'), note = document.getElementById('pvn');
  if (!input || !img) return;
  var oldSrc = img.getAttribute('src') || '', oldNote = note ? note.textContent : '', url = '';
  function reset() {
    if (url) { URL.revokeObjectURL(url); url = ''; }
    if (oldSrc) { img.src = oldSrc; img.hidden = false; if (ph) ph.hidden = true; }
    else { img.removeAttribute('src'); img.hidden = true; if (ph) ph.hidden = false; }
    if (note) { note.textContent = oldNote; note.classList.remove('is-new'); }
  }
  input.addEventListener('change', function () {
    var f = input.files && input.files[0];
    if (!f) { reset(); return; }
    if (!/^image\//.test(f.type)) { alert('Vui lòng chọn file hình ảnh (JPG, PNG, WEBP).'); input.value = ''; reset(); return; }
    if (f.size > 2 * 1024 * 1024) { alert('Ảnh tối đa 2MB. Vui lòng chọn ảnh nhỏ hơn.'); input.value = ''; reset(); return; }
    if (url) URL.revokeObjectURL(url);
    url = URL.createObjectURL(f);
    img.src = url; img.hidden = false; if (ph) ph.hidden = true;
    if (note) { note.textContent = 'Ảnh mới (xem trước): ' + f.name; note.classList.add('is-new'); }
  });
})();
