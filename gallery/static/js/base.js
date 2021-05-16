function CopyFunction() {
  var copyText = document.getElementById("imagelink");
  copyText.select();
  document.execCommand("copy");
  alert("Copied the text: " + copyText.value);
}