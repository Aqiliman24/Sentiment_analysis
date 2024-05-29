
  // Get Input from the Frontend when submit button clicked
function submitInput() {
  
    const inputString = document.getElementById('userInput').value;


    // live api - https://sentiment-analysis-lmeaghdm5a-as.a.run.app/chatbot
    // local api - http://127.0.0.1:8004/chatbot
    // Sending data to Backend
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
        if (data.includes('positive')) {
            responseMessage.textContent = "This sentence is mostly " + data;
            responseMessage.style.color = 'green';
        } else if (data.includes('negative')) {
            responseMessage.textContent = "This sentence is mostly " + data;
            responseMessage.style.color = 'red';
        } else if (data.includes('neutral')) {
            responseMessage.textContent = "This sentence is mostly " + data;
            responseMessage.style.color = 'gray';
        } else {
            responseMessage.textContent = data;
            responseMessage.style.color = 'black'; // default or for other cases
        }
    })
    .catch(error => console.error('Error:', error));
}

// Clear all input field when clear button clicked
function clearInput(){
    document.getElementById('userInput').value = '';
    document.getElementById('responseMessage').textContent  = '';
}
