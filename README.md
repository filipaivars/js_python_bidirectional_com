# js_python_bidirectional_com
Bidirectional Communication Between Javascript and Python

1. Launch Python server - `server.py`
    1. This will launch the python server
    2. Waiting for a message from the JS script (in-browser)
2. Launch `index.html`
    1. This will launch a webapp in your localhost
    2. `index.html` has `manager.js` script imported
    3. The JS script will send a message to your python server through port `8770`
    4. Once the message is sent, you'll be able to check you received the message in the terminal in which you launched the python server
    5. The python server will send back the same message received
    6. In your browser console you'll be able to see a log checking you received the return message from the python server
    7. Once you receive the message, the socket connection is closed

