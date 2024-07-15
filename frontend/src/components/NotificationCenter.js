import React from 'react';

const NotificationCenter = ({ notifications }) => (
    <div>
        <h3>Notifications</h3>
        {notifications.map((notification, index) => (
            <div key={index} className="notification">
                {notification.message}
            </div>
        ))}
    </div>
);

export default NotificationCenter;
