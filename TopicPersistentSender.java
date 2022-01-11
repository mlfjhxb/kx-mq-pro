package cn.knet.mq.mqtest.testing;

import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class TopicPersistentSender {
    //编写消息的发送方---消息的生产者

    public void send() throws Exception {
        //创建连接工厂对象
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("kxwz", "kx.wz123",
                "tcp://202.173.14.69:61616");
        //从工厂中获取连接对象
        Connection connection = connectionFactory.createConnection();
        //获得回话（session）对象
       TopicSession   session = (TopicSession)connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        //通过session对象创建Topic
        Topic topic = session.createTopic("itheimaTopic");
        //通过session对象创建消息的发送者
        TopicPublisher producer = (TopicPublisher)session.createPublisher(topic);
        producer.setDeliveryMode(DeliveryMode.PERSISTENT);
        connection.start();
        //连接MQ服务

        //通过session创建消息对象
        TextMessage message = session.createTextMessage("ping00");
        //发送消息
        producer.publish(message);

        //关闭相关资源
        producer.close();
        session.close();
        connection.close();
    }

    public static void main(String[] args) throws Exception {
        TopicPersistentSender obj=new TopicPersistentSender();
        obj.send();
    }
}
