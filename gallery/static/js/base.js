function copy() {
  $("#copy-url").select()
  document.execCommand('copy');
  alert("Image link copied to clipboard")
}