
window.onload = function (){
    loadDisplayMode();
    changeDisplayMode();
}

    // function to load dark mode if it is a YES on the DB. 
    function loadDisplayMode(){
        fetch('http://127.0.0.1:5000/dark_mode_load')
        .then(res=>res.json())
        .then (data =>{
            console.log(data);
            var darkSwitch = document.getElementById("flexSwitchCheckDefault");
            if (data['dark_mode'] == "YES"){
                document.body.setAttribute('data-bs-theme','dark');
                document.body.style.backgroundColor='#212529';
                darkSwitch.checked=true
            } 
            else {
                document.body.setAttribute('data-bs-theme','light');
                document.body.style.backgroundColor='';
                darkSwitch.checked=false
            }
        })
    }
    // function to update DB base on user input.

    function changeDisplayMode(){
        var darkSwitch = document.getElementById("flexSwitchCheckDefault");
        darkSwitch.addEventListener( "change", () => {
        if ( darkSwitch.checked ) {
            fetch('http://127.0.0.1:5000/dark_mode_change/YES')
            .then(res =>  res.json())
            .then(data => {loadDisplayMode()})
        } else {
            fetch('http://127.0.0.1:5000/dark_mode_change/NO')
            .then(res =>  res.json())
            .then(data => {loadDisplayMode()})
        }});
    }