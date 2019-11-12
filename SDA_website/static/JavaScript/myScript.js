function start(){
	document.getElementById("demo").innerHTML = "da";
}
function afisare(id) {
   var x = document.getElementById(id);
  // var str = x.innerHTML;
  // var leng = 100;
  // if(x.innerHTML.length > leng){
	// x.innerHTML = str.substring(4,leng);
  // }
  // else{
	// x.innerHTML = str;
  // }
  if (x.style.height === "100px") {
    x.style.height = "auto";
  } else {
    x.style.height	= "100px";
  }
} 