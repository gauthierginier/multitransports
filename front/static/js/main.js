// const search = document.getElementById('search');
// const matchlist = document.getElementById('match-list');


// const searchStation = async searchText => {
//     const res = await fetch("http://127.0.0.1:5000/Montpellier/stations/");
//     const stations = await res.json();

//     console.log(stations)
//     let matches = stations.filter(station =>{
//         const regex = new RegExp(`^${searchText}`, 'gi');
//         return station.Station.match(regex) || station.Ligne.match(regex)
//         ;

//     });
// if(searchText.length === 0){
//     matches = [];
// }

//     outputHtml(matches);
// };


// const outputHtml = matches => {
//     if(matches.length > 0){
//         const html = matches.map(match =>`
//             <div class = "card card-body mb-2">
//             <div class ="card-header">${match.Station}</div>
//                 <h6>Ligne : ${match.Ligne} Vers ${match.Direction}
//                 Prochain passage à : <span
//                 class="text-success">${match.Horaire}</span></h6>
//                 <small> Ville : ${match.Ville}</small>
//                 </div>

//                 `
//                 ).join('');
//             matchlist.innerHTML = html;
//     }
// }

// search.addEventListener('input', () =>searchStation(search.value))
// ;



const btnm = document.getElementById('button_montpellier');
const btnr = document.getElementById('button_rennes');
const search = document.getElementById('search');
const matchlist = document.getElementById('result');
var url = "http://127.0.0.1:5000/Montpellier/stations"
const selectCity = selectedcity => {
    url = "http://127.0.0.1:5000/"+selectedcity+"/stations"
    return "http://127.0.0.1:5000/"+selectedcity+"/stations"
    };

const searchStation = async (searchText, url) => {
    const res = await fetch(url);
    const stations = await res.json();

    console.log(stations)
    let matches = stations.filter(station =>{
        const regex = new RegExp(`^${searchText}`, 'gi');
        return station.Station.match(regex) || station.Ligne.match(regex)
        ;

    });
if(searchText.length === 0){
    matches = [];
}

    outputHtml(matches);
};


const outputHtml = matches => {
    if(matches.length > 0){
        const html = matches.map(match =>`
        <table class="table">
        <tbody>
          <tr class="table-active">
            <th scope="row">${match.Ligne}</th>
            <td>${match.Station}</td>
            <td>${match.Direction}</td>
            <td>${match.Horaire}</td>
          </tr>  </tbody>
          </table>

                `
                ).join('');
            matchlist.innerHTML = html;
    }
}

search.addEventListener('input', () =>searchStation(search.value, url ));
btnm.addEventListener('click', () =>selectCity(btnm.value));
btnr.addEventListener('click', () =>selectCity(btnr.value));
