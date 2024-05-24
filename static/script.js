
function clearInput(){
    document.getElementById('userInput').value = '';
    document.getElementById('responseMessage').textContent  = '';
}


function submitInput() {
    const inputString = document.getElementById('userInput').value;

    fetch('http://127.0.0.1:8004/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'
        },
        body: inputString
    })
    .then(response => response.text())
    .then(data => {
        const responseMessage = document.getElementById('responseMessage');

        responseMessage.textContent = "This sentence is mostly "+ data;
        responseMessage.style.color = 'green';
    })
    .catch(error => console.error('Error:', error));
}