/*Here we are setting up the variable isUserScrolling as False but if we use it it will stop the fetchin or messages*/
var isUserScrolling = false;
let scrollTimeout;

document.querySelector('.conversation-history').addEventListener('scroll', function() {
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

    fetch('http://127.0.0.1:5000/messages')
        .then(res =>  res.json())
        .then(data => {
            var messages = document.getElementById('conversationHistory');
            // var title_receiver = document.getElementById('title_receiver');
            var i_id = document.getElementById('user_id');
            // title_receiver.innerText = data[0]['t4.nick']
            messages.innerHTML=""
            for( let i = 0; i < data.length; i++){
                if (data[i].user_id == i_id.value){
                    messages.innerHTML += '<p class="text-sm-end col-10 ">'  + `<span style="color: #5B2F91; font-weight: bold;">You: </span>` + data[i].content + ` <i class="far fa-thumbs-up reaction-icon" onclick="toggleReaction(this)"></i></p>`;
                } else {
                    messages.innerHTML += '<p>' + `<span style="color: #5B2F91; font-weight: bold;">` +  data[i].nick + `: </span>` + data[i].content + ` <i class="far fa-thumbs-up reaction-icon" onclick="toggleReaction(this)"></i></p>`;
                
                }
            }
            messages.scrollTop = messages.scrollHeight;// Scroll to bottom after messages are added
        }
        )

}



getUsers();
setInterval(getUsers, 500);



function toggleReaction(icon) {
    if (icon.classList.contains('far') && icon.classList.contains('fa-thumbs-up')) {
        // Grey thumb up
        icon.classList.remove('far', 'fa-thumbs-up');
        icon.classList.add('fas', 'fa-thumbs-up');
        icon.style.color = '#5B2F91';
    } else if (icon.classList.contains('fas') && icon.classList.contains('fa-thumbs-up')) {
        // Purple thumb up
        icon.classList.remove('fas', 'fa-thumbs-up');
        icon.classList.add('fas', 'fa-thumbs-down');
        icon.style.color = '#5B2F91';
    } else if (icon.classList.contains('fas') && icon.classList.contains('fa-thumbs-down')) {
        // Purple thumb down
        icon.classList.remove('fas', 'fa-thumbs-down');
        icon.classList.add('far', 'fa-thumbs-up');
        icon.style.color = '#ccc';
    }
}
/* 
function sendMessage() {
    const messageInput = document.querySelector('.message-input');
    const conversationHistory = document.getElementById('conversationHistory');
    const message = document.createElement('div');
    message.classList.add('message');
    message.innerHTML = `<p>Sender: ${messageInput.value} <i class="far fa-thumbs-up reaction-icon" onclick="toggleReaction(this)"></i></p>`;
    conversationHistory.appendChild(message);
    messageInput.value = '';
} */
function eraseForm(){
    form=document.querySelector('#message').reset();
}

var message = document.getElementById('message');
        message.onsubmit = function(e){
            // "e" es el evento JS que ocurre cuando enviamos el formulario
            // e.preventDefault() es un método que detiene la naturaleza predeterminada de JavaScript
            e.preventDefault();
            // crea el objeto FormData desde JavaScript y envíalo a través de una solicitud post fetch
            var form = new FormData(message);
            // así es como configuramos una solicitud post y enviamos los datos del formulario
            fetch("http://localhost:5000/new_message", { method :'POST', body : form})
            .then( response => response.json() )
            .then(data => {
                eraseForm();// After the POST request is complete, call getUsers to update the user list
                getUsers();
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }