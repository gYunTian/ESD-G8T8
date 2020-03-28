async function run() {
    const res = await fetch('http://localhost:5002/initialize', {mode: 'cors'})
    
    if (res.status !== 200) {
        console.log('error')
    }
    else {
        const data = await res.json()
        let name = data['Name']
        let ticker = data['Ticker'].toUpperCase()
        $('#company').attr({class:'col-md-7 center-block col-centered'}).text(name + ' ('+ticker+')')   

        
        //loading
        $('#stock_price').text('').prepend( "<i class='fa fa-refresh fa-cog fa-spin'></i> Computing Price..." );
        $('#vix').text('').prepend( "<i class='fa fa-refresh fa-cog fa-spin'></i> Rerieving VIX..." );
        $('#general').text('').prepend( "<i class='fa fa-refresh fa-cog fa-spin'></i> Computing Sentiment..." );
        $('#stock_sentiment').text('').prepend( "<i class='fa fa-refresh fa-cog fa-spin'></i> Computing Stock Sentiment..." );
        $('#indicator').text('').prepend( "<i class='fa fa-refresh fa-cog fa-spin'></i> Plotting Chart..." );
        
        main()
    }           
}

$(document).ready(() => {
    run()
})

async function main() {
    const res = await fetch('http://localhost:5002/get_all', {mode: 'cors'})
    
    if (res.status !== 200) {
        console.log('error')
    }
    else {
        const data = await res.json()
        $('#vix').text('VIX: '+data['VIX'])
        $('#general').text('General Sentiment: '+data['General sentiment'])
        $('#stock_sentiment').text('Stock Sentiment: '+data['Stock sentiment'])
        $('#indicator').text('Indicators: '+data['RSI'])
        console.log(data)
    }    
}