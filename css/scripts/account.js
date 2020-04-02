$(document).ready( () => {
    get_all()

})

async function get_all() {
    const res = await fetch('http://localhost:5002/get_all', {mode: 'cors'})

    console.log('Pulling transactions')
    
    if (res.status !== 200) {
        console.log('error')
    }
    else {
        const data = await res.json()
        //all = JSON.stringify(data)
        console.log(data)
        data.forEach(([user, ticker, qty, price, action, unique]) => {
            if (unique.includes('sell')) {
                $('.table-striped').append('<tr>\
                <td>Sold</td>\
                <td>'+ticker+'</td>\
                <td>'+qty+'</td>\
                <td>'+price+'</td>\
                <td>Not implemented in this build</td>\
                </tr>')
            }
            else {
                $('.table-striped').append('<tr>\
                <td>Bought</td>\
                <td>'+ticker+'</td>\
                <td>'+qty+'</td>\
                <td>'+price+'</td>\
                <td>Not implemented in this build</td>\
                </tr>')
            }
            console.log(user, ticker, qty, price, action, unique)
        });
    }     
}