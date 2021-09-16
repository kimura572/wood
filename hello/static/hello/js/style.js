var elem2_1 = document.getElementById("area_hoge2");
var elem2_2 = document.getElementById("link_view2");
var elem2_3 = document.getElementById("link_hidden2");

elem2_1.style.display ="none";
elem2_2.style.display ="";
elem2_3.style.display ="none";

function toggle_view2() {
  elem2_1.style.display = "";
  elem2_2.style.display = "none";
  elem2_3.style.display = "";
}

function toggle_hidden2() {
  elem2_1.style.display = "none";
  elem2_2.style.display = "";
  elem2_3.style.display = "none";
}