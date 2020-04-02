/* JS for check ticker */

// async function checkTicker(value) {
//     const res = await fetch('http://localhost:5002/check/'+value, {mode: 'cors'})

//     if (res.status !== 200) {
//         $('#error').show().delay(3000).fadeOut('slow');
//         $('#search_ticker').attr('disabled',false).html("Search")
//         $('#search_input').attr('disabled',false);
//     }   
//     else {
//         const data = await res.json()
//         window.location.replace("./search.php");
//         //function ends
//     }

        
//         $('#error').text('Service is down! Try again later').show().delay(3000).fadeOut('slow');
//         $('#search_ticker').attr('disabled',false).html("Search")
//         $('#search_input').attr('disabled',false);
//     }

// }

async function checkTicker(value) {
    try { 
        let res = await timeoutPromise(60000, fetch('http://localhost:5002/check/'+value, {mode: 'cors'}));
        const data = await res.json()
        window.location.replace("./search.php");

        //function ends
    } catch(error) {
        //console.log(JSON.stringify(error))
        $('#error').text('Ticker not found! or Service might be down!').show().delay(5000).fadeOut('slow');

        $('#search_ticker').attr('disabled',false).html("Search")
        $('#search_input').attr('disabled',false);
    }
}

function timeoutPromise(ms, promise) {
    return new Promise((resolve, reject) => {
        const timeoutId = setTimeout(() => {
            reject(new Error("promise timeout"))
        }, ms);

        promise.then(
            (res) => {
                clearTimeout(timeoutId);
                resolve(res);
            },
            (err) => {
                clearTimeout(timeoutId);
                reject(err);
            }
        );
    })
}

/* Event Listeners */
$('#search_ticker').click(() => {
    $('#search_ticker').attr('disabled',true).text('').prepend( "<i class='fa fa-refresh fa-spin'></i> Searching..." );
    $('#search_input').attr('disabled',true);
    
    let ticker = $('#search_input').val()
    checkTicker(ticker)
});

