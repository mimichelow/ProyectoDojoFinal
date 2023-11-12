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
                .then(data => printMessage(data))
                .then(eraseForm());
        }