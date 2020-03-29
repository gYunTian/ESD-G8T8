
async function run() {
    const res = await fetch('http://localhost:5002/initialize', {mode: 'cors'})
    
    if (res.status !== 200) {
        console.log('error')
    }
    else {
        const data = await res.json()
        let name = data['Name']
        let ticker = data['Ticker'].toUpperCase()
        let current = data['Current']
        let input = name.toUpperCase()+' ('+ticker+'): $'+current
        $('#company').attr({class:'col-md-7 center-block col-centered'}).text(input)   
        //$('#company').text("").attr({class:'col-md-7 center-block col-centered'}).append( "<p style='color: #fff;   '>"+input+"</p>" );
            
        
        //loading
        $('#stock_price').text('').prepend("<p class='saving'>Computing Price <span>.</span><span>.</span><span>.</span></p><i class='fa fa-refresh fa-cog fa-spin'></i> " );
        $('#vix').text('').prepend( "<p class='saving'>Retrieving Volatility Index <span>.</span><span>.</span><span>.</span></p><i class='fa fa-refresh fa-cog fa-spin'>" );
        $('#general').text('').prepend( "<p class='saving'>Retrieving News & Computing Sentiment <span>.</span><span>.</span><span>.</span></p><i class='fa fa-refresh fa-cog fa-spin'></i>" );
        $('#stock_sentiment').text('').prepend( "<p class='saving'>Retrieving Stock News & Computing Sentiment <span>.</span><span>.</span><span>.</span></p><i class='fa fa-refresh fa-cog fa-spin'></i>" );
        $('#indicator').text('').prepend( "<p class='saving'>Plotting Chart <span>.</span><span>.</span><span>.</span></p><i class='fa fa-refresh fa-cog fa-spin'></i>" );
        $('#indicator2').text('').prepend( "<p class='saving'>Retrieving Indicators <span>.</span><span>.</span><span>.</span></p><i class='fa fa-refresh fa-cog fa-spin'></i>" );
        main()//.then(clear())
    }           
}   

async function main() {
    get2()
    get4()
    get5()
    get3()
    get6()
}

async function get2() {
    const res = await fetch('http://localhost:5002/get2', {mode: 'cors'})
    if (res.status !== 200) {
        console.log('error')
    }
    else {
        const data = await res.json()
        $('#stock_sentiment').text('Stock News Sentiment:').prepend( "" );
        if (data['sSentiment'].includes("-")) {
            $('#stock_sentiment').append( "<p style='color: #F23535;'>"+data['sSentiment']+"</p>" );
        }
        else {
            $('#stock_sentiment').append( "<p style='color: #71D980;'>"+data['sSentiment']+"</p>" );
        }
    }    
}

async function get3() {
    const res = await fetch('http://localhost:5002/get3', {mode: 'cors'})
    if (res.status !== 200) {
        $('#indicator2').text('Indicators:').prepend( "" );
        $('#indicator2').append( "<p>Exceeded API Limit of 5 Requests Per Minute</p>" );
    }
    else {
        const data = await res.json()
        $('#indicator2').text('Indicators:').prepend( "" );
        $('#indicator2').append( "<br><br><br><br>s<p>RSI: "+data['RSI']+"</p><br>" );
        $('#indicator2').append( "<p>MACD: "+data['MACD']+"</p><br>" );
        $('#indicator2').append( "<p>MACDS: "+data['MACD_S']+"</p><br>" );
    }    
}

async function get4() {
    const res = await fetch('http://localhost:5002/get4', {mode: 'cors'})
    if (res.status !== 200) {
        console.log('error')
    }   
    else {
        const data = await res.json()
        $('#general').text('General Market Sentiment:').prepend( "" );

        if (data['gSentiment'].includes("-")) {
            $('#general').append( "<p style='color: #F23535;'>"+data['gSentiment']+"</p>" );
        }
        else {
            $('#general').append( "<p style='color: #71D980;'>"+data['gSentiment']+"</p>" );
        }
    }    
}

async function get5() {
    const res = await fetch('http://localhost:5002/get5', {mode: 'cors'})
    if (res.status !== 200) {
        console.log('error')
    }
    else {
        const data = await res.json()
        $('#vix').text('Volatility Index:').prepend( "" );
        
        if (data['vix'] > 31) {
            $('#vix').append( "<p style='color: #F23535;'>"+data['vix']+"</p>" );
        }
        else {
            $('#vix').append( "<p style='color: #71D980;'>"+data['vix']+"</p>" );
        }
    }       
}

async function get6() {
    const res = await fetch('http://localhost:5002/get6', {mode: 'cors'})
    if (res.status !== 200) {
        console.log('error')
    }
    else {
        const data = await res.json()
        $('#indicator').text('').prepend( "Chart (300 days):" );  
        $('#indicator').append(data['data']);
    }       
}

// async function clear() {
//     const res = await fetch('http://localhost:5002/clear', {mode: 'cors'})
//     if (res.status !== 200) {
//         console.log('error')
//     }
//     console.log("Cleared!")
// }

$(document).ready(() => {
    run()
    $('[data-toggle="tooltip"]').tooltip();  
})