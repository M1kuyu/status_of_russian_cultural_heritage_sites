export const connectWebSocket = (onMessageCallback) => {
    const websocket = new WebSocket("ws://127.0.0.1:8000/ws/notifications/");

    websocket.onopen = () => {
        console.log("WebSocket connected");
    };

    websocket.onmessage = (event) => {
        onMessageCallback(event.data);
    };

    websocket.onerror = (error) => {
        console.error("WebSocket error:", error);
    };

    websocket.onclose = () => {
        console.log("WebSocket disconnected");
    };

    return websocket;
};


