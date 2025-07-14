const micButton = document.getElementById('micButton');
const statusDiv = document.getElementById('status');
const transcriptionDiv = document.getElementById('transcription');
const responseDiv = document.getElementById('response');

let mediaRecorder;
let audioChunks = [];

micButton.addEventListener('mousedown', startRecording);
micButton.addEventListener('mouseup', stopRecording);
micButton.addEventListener('touchstart', startRecording);
micButton.addEventListener('touchend', stopRecording);

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();
            statusDiv.textContent = 'Recording...';
            audioChunks = [];

            mediaRecorder.addEventListener('dataavailable', event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener('stop', () => {
                const audioBlob = new Blob(audioChunks);
                const audioUrl = URL.createObjectURL(audioBlob);
                const audio = new Audio(audioUrl);
                // audio.play(); // Uncomment to hear your recording
                sendAudioToServer(audioBlob);
            });
        });
}

function stopRecording() {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
        mediaRecorder.stop();
        statusDiv.textContent = 'Processing...';
    }
}

function sendAudioToServer(audioBlob) {
    const formData = new FormData();
    formData.append('audio_file', audioBlob, 'recording.wav');

    fetch('/api/voice-in-voice-out', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        statusDiv.textContent = '';
        transcriptionDiv.textContent = `You said: ${data.transcription}`;
        responseDiv.textContent = `VoccaTalk says: ${data.response}`;
    })
    .catch(error => {
        console.error('Error:', error);
        statusDiv.textContent = 'Error processing audio.';
    });
}
