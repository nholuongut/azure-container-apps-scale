import os
from time import sleep
from azure.servicebus import ServiceBusClient, AutoLockRenewer


connection_string = os.environ['SERVICE_BUS_CONNECTION_STRING']
queue_name = os.environ['QUEUE_NAME']

with ServiceBusClient.from_connection_string(connection_string, logging_enable=True) as client:
    with client.get_queue_receiver(queue_name) as receiver:
        with AutoLockRenewer(max_lock_renewal_duration=300) as renewer:

            # get a single message from the queue
            messages = receiver.receive_messages(max_message_count=1, max_wait_time=5)

            if not messages:
                print("No messages received. Exiting the job without processing anything.")
                exit(0)

            message = messages[0]

            # start the auto lock renewer for the message
            renewer.register(receiver, message)

            # process the message
            print("Received message: ", str(message))
            sleep(90)  # simulate processing time

            # complete the message
            receiver.complete_message(message)

            print("Message processed and completed. Exiting the job.")
