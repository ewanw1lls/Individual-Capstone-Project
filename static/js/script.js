
// document.getElementById('indoorButton').addEventListener('click', function () {
//     // Add pressed class to Indoor button and remove it from Outdoor button
//     this.classList.add('pressed');
//     document.getElementById('outdoorButton').classList.remove('pressed');
// });

// document.getElementById('outdoorButton').addEventListener('click', function () {
//     // Add pressed class to Outdoor button and remove it from Indoor button
//     this.classList.add('pressed');
//     document.getElementById('indoorButton').classList.remove('pressed');
// });

Microsoft.Maps.ConfigurableMap.createFromConfig(document.getElementById('myMap'), 'https://bingmapsisdk.blob.core.windows.net/isdksamples/configmap2.json', false, null, successCallback, errorCallback);
function successCallback(mapObj) {
    document.getElementById('printoutPanel').innerHTML = 'success';
}
function errorCallback(message) {
    document.getElementById('printoutPanel').innerHTML = message;
}