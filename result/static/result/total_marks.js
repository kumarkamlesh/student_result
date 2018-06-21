function total_marks(){
alert("yeahhhhh");
var a = document.getElementById("marks").value;
var b = document.getElementById("marks2").value;
var c = document.getElementById("marks3").value;
var d = document.getElementById("marks4").value;
var e = document.getElementById("marks5").value;
var f = document.getElementById("marks6").value;
var g = document.getElementById("marks7").value;
var h = document.getElementById("marks8").value;
var i = document.getElementById("marks9").value;
var j = document.getElementById("seminar").value;

//var k = document.getElementById("total").value;

num1 = +a;
num2 = +b;
num3 = +c;
num4 = +d;
num5 = +e;
num6 = +f;
num7 = +g;
num8 = +h;
num9 = +i;
num10 = +j;
//num11 = +k;
var ans = num1+num2+num3+num4+num5+num6+num7+num8+num9+num10;
var per = (ans*100)/1000;
if(ans){

document.getElementById("total").value = ans;
}

else
{
 alert("error");
}
if(per){
document.getElementById("percentage").value = per;

}
else
{
 alert("error");
}

}