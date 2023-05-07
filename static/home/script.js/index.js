var buttom_menu = document.querySelector('.buttom-menu');
var slidebar = document.querySelector('.sidebar');
var dashboard = document.querySelector('.dashboard');

buttom_menu.onclick = function () {
    slidebar.classList.toggle('zoom-out');
    dashboard.classList.toggle('zoom-in');
}
// CALCULATOR
const numbers = document.getElementsByClassName('btn');
const result = document.getElementById('result');

for (const number of numbers) {
    number.addEventListener('click', function () {
        result.innerHTML += this.value;
    });
}
function equal() {
    let res = result.innerHTML;
    let output = eval(res);
    result.innerHTML = output;
}
function clean() {
    result.innerHTML = " ";
}
function undo() {
    let res = result.innerHTML;
    result.innerHTML = res.substring(0, res.length - 1);
}

// CLICK SHOW CALCULATOR
const blur_cal=document.querySelector('#blur-cal');
const cal=document.querySelector('.calcula');

cal.onclick=function(){
    blur_cal.classList.add('show_cal');
}
// CLICK HIDE CALCULATOR
const close=document.querySelector('.ic-close');
const shutcal=document.querySelector('.footer-shutcal');

close.onclick=function(){
    blur_cal.classList.remove('show_cal');
}

shutcal.onclick=function(){
    blur_cal.classList.remove('show_cal');
}
// CLICK SHOW CALCULATOR
const blur_text=document.querySelector('#blur-text');
const text=document.querySelector('.text');

text.onclick=function(){
    blur_text.classList.add('show_text');
}
// CLICK HIDE CALCULATOR
const close_text=document.querySelector('.ic-close-text');
const save=document.querySelector('.footer-save');
const shut=document.querySelector('.footer-shut');
close_text.onclick=function(){
    blur_text.classList.remove('show_text');
}
save.onclick=function(){
    blur_text.classList.remove('show_text');
    alert("Lưu thành công");
}
shut.onclick=function(){
    blur_text.classList.remove('show_text');
}
// STATUS CHART

var barColors = [
  "rgb(54, 162, 235)",
  "rgb(255, 99, 132)",
];

function create_status_room(yValues){
  var xValues = ["Đang thuê", "Phòng trống"];
  
  new Chart("statusChart", {
    type: "pie",
    data: {
      labels: xValues,
      datasets: [{
        backgroundColor: barColors,
        data: yValues
      }]
    },
    options: {
      title: {
        display: true,
      }
    }
  });
}

// TURNOVER CHART
var xValues = ["T1","T2","T3","T4","T5","T6","T7","T8","T9","T10","T11","T12"];
var yValues = [7,8,8,9,9,9,10,11,14,14,15,9];

new Chart("turnoverChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(0,0,255,1.0)",
      borderColor: "rgba(0,0,255,0.1)",
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    scales: {
      yAxes: [{ticks: {min: 6, max:16}}],
    }
  }
});



