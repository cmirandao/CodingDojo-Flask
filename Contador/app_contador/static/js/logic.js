let input = document.querySelector(".input");
let button = document.querySelector(".btn btn-primary btn-lg btn-block");
button.disabled = true;
input.addEventListener("change", stateHandle);
function stateHandle() {
    if (document.querySelector(".input").value === "") {
        button.disabled = true; 
    } else {
        button.disabled = false;
    }
}