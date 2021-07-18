var nav = document.getElementsByClassName("find");

nav[0].style.color="green";
nav[0].style.backgroundColor="white";
nav[0].style.borderRadius="30px";
nav[0].style.boxShadow="rgb(0, 0, 0, 50%) 2px 2px 10px";

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

    cnp=nnp
}