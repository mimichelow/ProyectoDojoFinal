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

function sendMessage() {
    const messageInput = document.querySelector('.message-input');
    const conversationHistory = document.getElementById('conversationHistory');
    const message = document.createElement('div');
    message.classList.add('message');
    message.innerHTML = `<p>Sender: ${messageInput.value} <i class="far fa-thumbs-up reaction-icon" onclick="toggleReaction(this)"></i></p>`;
    conversationHistory.appendChild(message);
    messageInput.value = '';
}