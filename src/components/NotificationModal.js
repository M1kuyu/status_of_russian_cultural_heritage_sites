import { useEffect, useState } from "react";
import { io } from "socket.io-client";

const NotificationModal = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    const socket = io("http://localhost:8000");
    socket.on("update", (data) => {
      setNotifications((prev) => [...prev, data]);
    });

    return () => socket.disconnect();
  }, []);

  return (
    <div>
      <h3>Notifications</h3>
      <ul>
        {notifications.map((note, index) => (
          <li key={index}>{note.message}</li>
        ))}
      </ul>
    </div>
  );
};

export default NotificationModal;
