$(document).ready( () => {

    console.log('ready')
    $("#retrieve").click(function() {
        $('#hide').hide()
        $(this).attr('disabled',true).prepend( "<span id='show'>Retrieving.. <i class='fa fa-refresh fa-spin'></i></span>" );
        retrieve()
    })


    $("#clear_transactions").click(function() {
        console.log('clearing transactions')
        $('#clear_hide').hide()
        $(this).attr('disabled',true).prepend( "<span id='clear_show'>Clearing... <i class='fa fa-refresh fa-spin'></i></span>" );
        transaction()
    })
})


async function retrieve() {
    const res = await fetch('http://localhost:5500/retrieve', {mode: 'cors'})
    
    
    console.log('Pulling transactions')
    
    if (res.status !== 200) {
        console.log('error')
    }
    else {
        const data = await res.json()

        if (data['status'] == 'No message in queue') {
            $('#empty').show().text('No transactions found')
        }
        else {
            $('#add').append(data['data'])
            $('#empty').hide()
        }
        $('#retrieve').attr('disabled',false)
        $('#show').hide()
        $('#hide').show()
    }     
}

async function transaction() {
    // $('checkbox:checked')
    var spans = document.getElementsByClassName('pick')
    var ids = []
    for (var i=0; i < spans.length; ++i){
        ids.push(spans[i].id)
    }
    console.log(ids)
    
}