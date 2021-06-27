//ProgressBars
 options = {
    startAngle: -1.5,
    size: 250,
    fill: {gradient: ["#fc1f3c", "#652efc", "#2dfa7c"]}
}

function setC1(x) {
    if (x.matches) { 
        options = {
            startAngle: -1.5,
            size: 150,
            fill: {gradient: ["#fc1f3c", "#652efc", "#2dfa7c"]}
        }
        $(".circle .bar").circleProgress(options).on('circle-animation-progress',
        function(event, progress, stepValue) {
            $(this).parent().find("span").text(String(stepValue.toFixed(2).substr(2)+ "%"))
        });
    } else {
        options = {
            startAngle: -1.5,
            size: 250,
            fill: {gradient: ["#fc1f3c", "#652efc", "#2dfa7c"]}
        }
        $(".circle .bar").circleProgress(options).on('circle-animation-progress',
        function(event, progress, stepValue) {
            $(this).parent().find("span").text(String(stepValue.toFixed(2).substr(2)+ "%"))
        });
    }
}
var mediaQ1 = window.matchMedia("(max-width: 1475px)")
setC1(mediaQ1) 
mediaQ1.addListener(setC1) /

$(".circle .bar").circleProgress(options).on('circle-animation-progress',
function(event, progress, stepValue) {
    $(this).parent().find("span").text(String(stepValue.toFixed(2).substr(2)+ "%"))
});
$(".S .bar").circleProgress({
    value: .90
})
$(".U .bar").circleProgress({
    value: .99
})
$(".B .bar").circleProgress({
    value: .55
})
$(".G .bar").circleProgress({
    value: .75
})
$(".W .bar").circleProgress({
    value: .35
})
$(".C .bar").circleProgress({
    value: .85
})
$(".H .bar").circleProgress({
    value: .80
})
$(".R .bar").circleProgress({
    value: .70
})
$(".N .bar").circleProgress({
    value: .88
})