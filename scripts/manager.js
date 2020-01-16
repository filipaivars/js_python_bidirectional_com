var socket = new WebSocket('ws://localhost:8770/');

socket.onopen = function(event){
    socket.send('Hi');
};

socket.onmessage = function(event){
    console.log("Message Received!");
    console.log(event.data);
    socket.close()          // this can be placed wherever it fits in your logic
};

socket.onclose = function(event) {
    if (event.wasClean) {
        console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    } else {
        // e.g. server process killed or network down
        // event.code is usually 1006 in this case
        console.log('[close] Connection died');
    }
};

socket.onerror = function(error) {
    console.log(`[error] ${error.message}`);
};