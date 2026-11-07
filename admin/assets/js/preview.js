/* Xem trước ảnh sản phẩm ngay khi chọn file.
   Đây là đoạn JavaScript duy nhất của website và chỉ dùng để xem trước ảnh:
   không kiểm tra, không lưu hay đọc dữ liệu nào. */
(function () {
  var input = document.getElementById('pimg'), img = document.getElementById('pimgv'),
      ph = document.getElementById('pph'), note = document.getElementById('pvn');
  if (!input || !img) return;
  input.addEventListener('change', function () {
    var f = input.files && input.files[0];
    if (!f) return;
    img.src = URL.createObjectURL(f);
    img.hidden = false;
    if (ph) ph.hidden = true;
    if (note) note.textContent = 'Ảnh mới (xem trước): ' + f.name;
  });
})();
