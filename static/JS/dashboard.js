//ProgressBars
 options = {
    startAngle: -1.5,
    size: 250,
    value: .75,
    fill: {gradient: ["#fc1f3c", "#652efc", "#2dfa7c"]}
}

function setC1(x) {
    if (x.matches) { 
        options = {
            startAngle: -1.5,
            size: 150,
            value: .75,
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
            value: .75,
            fill: {gradient: ["#fc1f3c", "#652efc", "#2dfa7c"]}
        }
        $(".circle .bar").circleProgress(options).on('circle-animation-progress',
        function(event, progress, stepValue) {
        });
    }
}
var mediaQ1 = window.matchMedia("(max-width: 1475px)")
setC1(mediaQ1) 
mediaQ1.addListener(setC1) 