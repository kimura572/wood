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

var nameList = [
  'satou', 'suzuki', 'tanaka', 'takahashi', 'itou', 'yamamoto', 'watanabe', 'nakamura', 'kobayashi', 'katou',
  'yoshida', 'yamada', 'sasaki', 'yamaguchi', 'matsumoto', 'inoue', 'kimura', 'hayashi', 'saitou', 'shimizu',
  'yamazaki', 'abe', 'mori', 'ikeda', 'hashimoto', 'yamashita', 'ishikawa', 'nakajima', 'maeda', 'fujita',
  'gotou', 'ogawa', 'okada', 'murakami', 'hasegawa', 'kondou', 'ishii', 'sakamoto', 'endou', 'fujii'
];

function f(){
  for(var i=0;i<nameList.length;i++){
    let op = document.createElement("option");
    op.value = nameList[i];
    document.getElementById("dt1").appendChild(op);
  }
}