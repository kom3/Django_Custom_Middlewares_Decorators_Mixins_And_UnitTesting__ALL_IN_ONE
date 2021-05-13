function callfunc() {
    alert('Hi, you called me?')
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function login() {
    // console.log(getCookie('csrftoken'))
    let username = $('#username').val()
    let password = $('#password').val()
    let data = {
        // fetch API call
        headers: { "Content-Type": "application/json", "X-CSRFTOKEN": getCookie('csrftoken') },
        method: "POST",
        body: JSON.stringify({ "username": username, "password": password })
    }

    fetch("login", data).then(res => console.log(res.json()))

}

