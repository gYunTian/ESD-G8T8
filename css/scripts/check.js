/* JS for check ticker */

async function checkTicker(value) {
    const res = await fetch('http://localhost:5002/check/'+value, {mode: 'cors'})
    
    if (res.status !== 200) {
        $('#error').show().delay(3000).fadeOut('slow');
        $('#search_ticker').attr('disabled',false).html("Search")
        $('#search_input').attr('disabled',false);
    }   
    else {
        const data = await res.json()
        window.location.replace("./search.html");
        //function ends
    }
}

/* Event Listeners */
$('#search_ticker').click(() => {
    $('#search_ticker').attr('disabled',true).text('').prepend( "<i class='fa fa-refresh fa-spin'></i> Searching..." );
    $('#search_input').attr('disabled',true);
    
    let ticker = $('#search_input').val()
    checkTicker(ticker)
});

