/*Here we are setting up the variable isUserScrolling as False but if we use it it will stop the fetchin or messages*/
var isUserScrolling = false;
let scrollTimeout;

document.querySelector('#chats_history').addEventListener('scroll', function() {
    isUserScrolling = true;
    // Clear the previous timeout
    clearTimeout(scrollTimeout);
    // Set a timeout to reset the flag after 5 second of inactivity
    scrollTimeout = setTimeout(function() {
        isUserScrolling = false;
    }, 5000);
});

function getUsers(){
    if (isUserScrolling) {
        return;
    }

    fetch('http://127.0.0.1:5000/chats_dash_ajax')
        .then(res =>  res.json())
        .then(data => {
            var chats = document.getElementById('chats_history');
            chats.innerHTML=""
            for( let i = 0; i < data.length; i++){
                if (data[i].user_dash == data[i]['t4.id']){
                    temp = data[i].fname;
                    data[i].fname = data[i]['t4.fname'];
                    data[i]['t4.fname'] = temp;
                    temp = data[i].lname;
                    data[i].lname = data[i]['t4.lname'];
                    data[i]['t4.lname'] = temp;
                    temp = data[i].email;
                    data[i].email = data[i]['t4.email'];
                    data[i]['t4.email'] = temp;
                    temp = data[i].nick;
                    data[i].nick = data[i]['t4.nick'];
                    data[i]['t4.nick'] = temp;
                    temp = data[i].picture;
                    data[i].picture = data[i]['t4.picture'];
                    data[i]['t4.picture'] = temp;
                } 
                if (data[i].seen == null){
                    data[i].seen = 0
                }
                if (data[i].seen == 0){
                    seen = `<p class="rounded-circle col-1 text-center fs-5 pt-1  " style="width:40px;height:40px; color:white" ></p>`
                } else {
                    seen = `<p class="rounded-circle col-1 text-center fs-5 pt-1  " style="width:40px;height:40px;background-color:#F99417; color:white" >` + data[i].seen + `</p>`
                }
                chats.innerHTML += `<a href="/chats/` + data[i].chat_id + `" class="text-reset text-decoration-none">
                <div class="rounded col-11 chat-box container border border-2 mt-4 d-flex align-items-center justify-content-between">
                    <div class="sender-img">
                        <img class="rounded-circle" src="../static/uploads/` + data[i]['t4.picture'] + `">
                        </div>
                        <div class="mt-3 ms-3 col-9">
                            <p class="fw-bold fs-5 ">` + data[i]['t4.fname'] + " " + data[i]['t4.lname'] + `</p>
                            <div class="d-flex justify-content-between"><p >` + data[i].content + ` </p> <p >` + data[i].timestamp + `</p></div>`   +   
                            `</div>` + seen + `        </div>
                            </a>`
                // chats.innerHTML += '<div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">' + `<a href="/chat/${data[i].id}">` + `<div class="card" style="width: 18rem;">` + `<img src="${data[i].image}" class="card-img-top" alt="...">` + `<div class="card-body">` + `<h5 class="card-title">${data[i].name}</h5>` + `<p class="card-text">${data[i].description}</p>` + `</div>` + `</div>` + `</a>` + `</div>`;
            }
        }
        )

}



getUsers();
setInterval(getUsers, 500);


