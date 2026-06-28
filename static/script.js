const form = document.getElementById("loginForm");
const loading = document.getElementById("loading");

form.addEventListener("submit", function(e){

    e.preventDefault();

    loading.style.display = "block";

    const messages = loading.querySelectorAll("p");

    messages.forEach(msg=>{
        msg.style.opacity = "0.3";
        msg.innerHTML = msg.innerHTML.replace("✔ ","");
    });

    let i = 0;

    const interval = setInterval(()=>{

        messages[i].style.opacity = "1";
        messages[i].innerHTML = "✔ " + messages[i].innerHTML;

        i++;

        if(i===messages.length){

            clearInterval(interval);

            setTimeout(()=>{

                form.submit();

            },600);

        }

    },500);

});