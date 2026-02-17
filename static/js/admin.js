function deleteProduct(by) {
  let text = "Are you sure to delete all products?";
  if (confirm(text) == true) {
    window.location.href = '/admin/delete/?by='+by;
  } 
}