from confluent_kafka import Consumer



c=Consumer({
    'bootstrap.servers':'localhost:9092',
    'group.id':'email_notification_group',
    'auto.offset.reset':'earliest'
})

c.subscribe(['email_notifications'])


while True:
    msg=c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error:{msg.error()}")
        continue
    print(f"Received email notification:{msg.value().decode('utf-8')}")