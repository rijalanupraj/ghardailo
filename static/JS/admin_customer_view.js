var nav = document.getElementsByClassName("find");
var navdiv = document.getElementsByClassName("navdiv");
var counter = document.getElementsByClassName("counter");

nav[0].style.color="green";
nav[0].style.backgroundColor="white";
nav[0].style.borderRadius="30px";
nav[0].style.boxShadow="rgb(0, 0, 0, 50%) 2px 2px 10px";

navdiv[1].style.display="none";
navdiv[2].style.display="none";
navdiv[3].style.display="none";

counter[0].style.display="none";
counter[1].style.display="none";
counter[2].style.display="none";

var cnp = 0;
function navigate(nnp) {
    nav[cnp].style.color="white";
    nav[cnp].style.backgroundColor="transparent";
    nav[cnp].style.borderRadius="0px";
    nav[cnp].style.boxShadow="rgb(0, 0, 0, 50%) 0px 0px 0px";
    
    nav[nnp].style.color="green";
    nav[nnp].style.backgroundColor="white";
    nav[nnp].style.borderRadius="30px";
    nav[nnp].style.boxShadow="rgb(0, 0, 0, 50%) 2px 2px 10px";

    navdiv[cnp].style.display="none";
    navdiv[nnp].style.display="block";

    if (nnp!=0) {        
        counter[nnp-1].style.display="block";
    }
    if (cnp!=0) {        
        counter[cnp-1].style.display="none";
    }

    cnp=nnp
}

var hire_number = document.getElementsByClassName("Numbering1").length
for (i=0; i<hire_number; i++) {
    document.getElementsByClassName("Numbering1")[i].innerHTML = i + 1
}
var notification_number = document.getElementsByClassName("Numbering2").length
for (i=0; i<notification_number; i++) {
    document.getElementsByClassName("Numbering2")[i].innerHTML = i + 1
}
var review_number = document.getElementsByClassName("Numbering3").length
for (i=0; i<review_number; i++) {
    document.getElementsByClassName("Numbering3")[i].innerHTML = i + 1
}