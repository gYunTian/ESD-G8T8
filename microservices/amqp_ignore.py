    #external APIS
    #will use amqp

    #non api
    #sentiment - http
    
    #UI to middleware
    #promise with loading indicator
    #https://javascript.info/promise-basics
    
    
    import pika

    connection = pika.BlockingConnection()

    channel = connection.channel()

    channel.exchange_declare()

    channel.queue_declare()

    channel.queue_bind()

    