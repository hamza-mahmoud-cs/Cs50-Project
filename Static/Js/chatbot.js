document.getElementById('chatform').addEventListener('submit', async function(e) {
    e.preventDefault();
    const input = document.getElementById('userInput');
    const chatbox = document.getElementById('chatbox');
    const message = input.value.trim();
    
    if (!message) return;

    chatbox.innerHTML += `<div class='message user-msg'><b>you:</b> ${message}</div>`;
    input.value= '';
    chatbox.scrollTop = chatbox.scrollHeight;

    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message ai-msg';
    loadingDiv.innerText = 'thinking...';
    chatbox.appendChild(loadingDiv)

    try {
        const response = await fetch('/ai', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({message: message})
        }
        );
        const data = await response.json();
        loadingDiv.innerHTML = `<b> AI:</b> ${data.reply}`;
    } catch (error) {
        loadingDiv.innerText = 'there is a problem with your connection';
    }
    chatbox.scrollTop = chatbox.scrollHeight;
});