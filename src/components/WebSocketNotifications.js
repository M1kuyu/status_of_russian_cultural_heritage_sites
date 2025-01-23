
import React, { useEffect } from "react";
import { connectWebSocket } from "../api/websocket";

const WebSocketNotifications = () => {
    useEffect(() => {
        const websocket = connectWebSocket((message) => {
            console.log("Notification received:", message);
        });

        return () => websocket.close();
    }, []);

    return <div>WebSocket Notifications are connected!</div>;
};

export default WebSocketNotifications;

