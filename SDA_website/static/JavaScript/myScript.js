function afisare(id) {
	// face elementele de height auto -- pt sertarase
  var x = document.getElementById(id);
  if (x.style.height === "100px") {
    x.style.height = "auto";
  } else {
    x.style.height	= "100px";
  }
} 