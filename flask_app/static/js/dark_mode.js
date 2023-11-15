window.onload=function () {
    let darkSwitch = document.getElementById('flexSwitchCheckDefault');
    darkSwitch.addEventListener( "change", () => {
        if ( darkSwitch.checked ) {
            document.body.setAttribute('data-bs-theme','dark')
            document.body.style.backgroundColor='#212529';
        } else {
            document.body.setAttribute('data-bs-theme','light')
            document.body.style.backgroundColor='';
        }
    });
}