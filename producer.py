from confluent_kafka import Producer

p=Producer({'bootstrap.servers': 'localhost:9092'})


def send_notification(topic,email_payload):
    p.produce(topic, email_payload.encode('utf-8'))
    p.poll(0)
    p.flush()
    print(f'email notifiaction sent to the tpic:{topic} and payload:{email_payload}')

email_payload = '{"to":"receiver@example.com","from":"sender@example.com","subject":test_email,"body":"This is a test email."}'
send_notification('email_notifications', email_payload)


