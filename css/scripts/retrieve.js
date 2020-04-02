$(document).ready( () => {

    console.log('ready')
    $("#retrieve").click(function() {
        $('#hide').hide()
        $(this).attr('disabled',true).prepend( "<span id='show'>Retrieving.. <i class='fa fa-refresh fa-spin'></i></span>" );
        retrieve()
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