async function checkInternet(){
    await eel.check_internet();
}

var connectionStatus;
function isThereInternet(){

    var online = navigator.onLine;
    var alert = document.getElementById('alert')
    var screenshotBtn = document.getElementById('screenshot');

    connectionStatus = online ? "True":"False"

    if(online){

        screenshotBtn.disabled = false;
        alert.classList.remove('d-none');
        alert.classList.remove('alert-danger');
        alert.innerHTML = '<i class="fas fa-circle small text-success mr-3"></i>You are connected to Internet.'
        alert.classList.add('alert-success');

    }else{

        screenshotBtn.disabled = true;
        alert.classList.remove('d-none');
        alert.classList.remove('alert-success');
        alert.innerHTML = '<i class="fas fa-circle small text-danger mr-3"></i>You are not connected to Internet.'
        alert.classList.add('alert-danger');

    }
}

async function screenshot(){

        var web_address = document.getElementById("web-address").value;
        var statusBar = document.getElementById('status')

        var e = document.getElementById('protocol');
        var protocol_value = e.options[e.selectedIndex].value;
        var link;
        var protocol;

        switch(protocol_value){
            case "0": protocol = "";
                    break;
            case "1": protocol = "http://";
                    break;
            case "2": protocol = "https://";
                    break;
            case "3": protocol = "file:///";
                    break;
            default: protocol = ""
        }


        if(protocol == ""){

            statusBar.innerHTML = "Please select protocol";

        }else if(web_address == ""){

            statusBar.innerHTML = "Enter URL";

        }else if(protocol == "file:///"){

            link = protocol + web_address;

            var driverStatus = await eel.open_browser(connectionStatus)();
            statusBar.innerHTML = driverStatus;

            var result = await eel.screenshot(link)();
            statusBar.innerHTML = result;

        }else{

            link = protocol + web_address;

            var driverStatus = await eel.open_browser(connectionStatus)();
            statusBar.innerHTML = driverStatus;

            var result = await eel.check_url(link, connectionStatus)();
            statusBar.innerHTML = result;
        }
}

window.onload = isThereInternet;
setInterval(isThereInternet, 5000)