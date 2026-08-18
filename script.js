function copyText(id, button){

    const text = document.getElementById(id).innerText;

    navigator.clipboard.writeText(text);

    const original = button.innerHTML;

    button.innerHTML = "✓ Copied";
    button.disabled = true;

    setTimeout(function(){

        button.innerHTML = original;
        button.disabled = false;

    }, 2000);

}

function clearResults(){

    document.querySelector("textarea").value = "";

    const results = document.querySelector(".results");

    if(results){
        results.style.display = "none";
    }

}
