let finalresult

navigator.geolocation.getCurrentPosition(
   function (position) {
      initMap(position.coords.latitude, position.coords.longitude)
   },
   function errorCallback(error) {
      console.log(error)
   }
);

function initMap(lat, lng) {

   var myLatLng = {
      lat,
      lng
   };

   var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15,
      center: myLatLng
   });

   var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,

   });


var requestOptions = {
    method: 'GET',
    redirect: 'follow'
  };
 
  fetch(`http://api.airvisual.com/v2/nearest_city?lat=${lat}&lon=${lng}&key=a887e633-82c9-4b3e-9aea-bd8507be1a15`, requestOptions)
    .then(response => response.text())
    .then(result => { 
      //  console.log(typeof result);
       resultfinal=JSON.parse(result)
       console.log(resultfinal.data.current.pollution.aqius);
      })
    .catch(error => console.log('error', error));


let div=document.getElementById('data');
div.innerText = resultfinal.data.current.pollution.aqius ;

document.getElementById("data").style.color="#ecdc1d";
document.getElementById("data").style.fontSize="200px";
}

