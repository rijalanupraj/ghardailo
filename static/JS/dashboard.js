nav_height = document.getElementById("Header").offsetHeight
document.getElementsByClassName('sidebar_nav')[0].style.top = nav_height+'px' 

//Toggling offcanvas opening button
offcanvas_check = false
function hideOp(){
    document.getElementById("Items").style.paddingInlineStart = (document.getElementsByClassName('sidebar_nav')[0].clientWidth+8) + "px"
    document.getElementById("offcanvas_opener").style.visibility = "hidden"
    offcanvas_check = true
}
function showOp(){
    document.getElementById("Items").style.paddingInlineStart = "5px"
    document.getElementById("offcanvas_opener").style.visibility = "visible"
    offcanvas_check = false
}

//Setting up offcanvas height according to navbar height
var nav_check = true
function setH(){
    if (nav_check) {
        nav_height1 = document.getElementById("Header").offsetHeight 
        document.getElementsByClassName('sidebar_nav')[0].style.top = nav_height1+'px' 
        nav_check = false
    }
    else {
        document.getElementsByClassName('sidebar_nav')[0].style.top = nav_height+'px' 
        nav_check = true
    }
}

// Media Query for offcanvas and items
function setH1(x) {
    if (x.matches) { // If media query matches
        nav_height1 = document.getElementById("Header").offsetHeight 
        document.getElementsByClassName('sidebar_nav')[0].style.top = nav_height1+'px' 
        if(offcanvas_check) {            
            document.getElementById("Items").style.paddingInlineStart = (document.getElementsByClassName('sidebar_nav')[0].clientWidth+8) + "px"
        }
        else {            
            document.getElementById("Items").style.paddingInlineStart = "5px"
        }
    } else {
        document.getElementsByClassName('sidebar_nav')[0].style.top = nav_height+'px' 
        if(offcanvas_check) {            
            document.getElementById("Items").style.paddingInlineStart = (document.getElementsByClassName('sidebar_nav')[0].clientWidth+8) + "px"
        }
        else {            
            document.getElementById("Items").style.paddingInlineStart = "5px"
        }
    }
}
var mediaQ = window.matchMedia("(max-width: 575px)")
setH1(mediaQ) // Call listener function at run time
mediaQ.addListener(setH1) // Attach listener function on state changes
