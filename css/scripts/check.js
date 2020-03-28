/* JS for check ticker */

async function checkTicker(value) {
    const res = await fetch('http://localhost:5010/check/'+value, {mode: 'cors'})

    if (res.status !== 200) {
        //console.log("Not found!")
        $('#error').show().delay(3000).fadeOut('slow');
    }
    else {
        const data = await res.json()
        console.log(data)
    }
    $('#search_ticker').attr('disabled',false).html("Search")
    $('#search_input').attr('disabled',false);

}

$('#search_ticker').click(() => {
    $('#search_ticker').attr('disabled',true).html("Searching...")
    $('#search_input').attr('disabled',true);
    
    let ticker = $('#search_input').val()
    checkTicker(ticker)
});
