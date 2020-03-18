let scanner = new Instascan.Scanner({ video: document.getElementById('preview'), mirror: false});
scanner.addListener('scan', function (content) {
    window.location.replace(`/scanned/${content}`);
});
Instascan.Camera.getCameras().then(function (cameras) {
    if (cameras.length > 0) {
        scanner.start(cameras[cameras.length - 1]);
    } else {
        console.error('No cameras found.');
    }
}).catch(function (e) {
    console.error(e);
});