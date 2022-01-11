package cn.knet.mq.mqtest.testing;

import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class MqTopicProducter {
    public static void main(String[] args) throws JMSException {


        // ConnectionFactory ：连接工厂，JMS 用它创建连接
        ConnectionFactory connectionFactory =
                new ActiveMQConnectionFactory("kxwz", "kx.wz123",
                        "tcp://202.173.14.69:61616");
        // JMS 客户端到JMS Provider 的连接
        Connection connection = connectionFactory.createConnection();
        // Session： 一个发送或接收消息的线程
        TopicSession session = (TopicSession) connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        // Destination ：消息的目的地;消息发送给谁.
        // 获取session注意参数值my-queue是Query的名字
        Topic destination = session.createTopic("my-topic");
        // MessageProducer：消息生产者
        TopicPublisher producer = session.createPublisher(destination);
        connection.start();
        // 默认设置是持久化
//        producer.setDeliveryMode(DeliveryMode.PERSISTENT);
        // 发送一条消息
        for (int i = 1; i <= 1; i++) {
            // 创建一条文本消息
            TextMessage message = session.createTextMessage("my first topic" + i);
// 通过消息生产者发出消息
            producer.publish(message);

        }
        producer.close();
//        session.commit();
        session.close();
        connection.close();

    }

    /**
     *        * 在指定的会话上，通过指定的消息生产者发出一条消息
     * <p>
     *        *
     * <p>
     *        * @param session
     * <p>
     *        * 消息会话
     * <p>
     *        * @param producer
     * <p>
     *        * 消息生产者
     * <p>
     *        
     */
    public static void sendMsg(Session session, MessageProducer producer, int i) throws JMSException {
// 创建一条文本消息
        TextMessage message = session.createTextMessage("Hello ActiveMQ！" + i);
// 通过消息生产者发出消息
        producer.send(message);
    }
}
