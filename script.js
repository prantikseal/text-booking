document.getElementById('book').addEventListener('click', () => {
    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = true;

        recognition.onresult = (event) => {
            const result = event.results[event.results.length - 1][0].transcript;

            // Send the recorded audio data to your Flask backend via a POST request
            fetch('/book', {
                method: 'POST',
                body: JSON.stringify({ audio_data: result }),
                headers: { 'Content-Type': 'application/json' },
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the server
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });

            recognition.stop();
        };

        recognition.start();
    } else {
        alert('Your browser does not support the Web Speech API.');
    }
});
