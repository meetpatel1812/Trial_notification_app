// Register Service Worker
if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("service-worker.js")
        .then(() => console.log("Service Worker Registered"))
        .catch(err => console.log("Service Worker Registration Failed: ", err));
}

// Request Notification Permission
document.getElementById("enable-notifications").addEventListener("click", () => {
    Notification.requestPermission().then(permission => {
        if (permission === "granted") {
            console.log("Notification permission granted.");
        }
    });
});

// Listen for Notifications
if ("serviceWorker" in navigator) {
    navigator.serviceWorker.ready.then(registration => {
        registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: "your-vapid-public-key"
        }).then(subscription => {
            console.log("Push Subscription: ", subscription);
        });
    });
}