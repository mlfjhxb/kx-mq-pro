package cn.knet.mq.mqtest.testing;

import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class MqTopicReceiver1 {
    public static void main(String[] args) throws JMSException {
        // ConnectionFactory ：连接工厂，JMS 用它创建连接
        ConnectionFactory connectionFactory =
                new ActiveMQConnectionFactory("kxwz", "kx.wz123",
                        "tcp://202.173.14.69:61616");
        // JMS 客户端到JMS Provider 的连接
        Connection connection = connectionFactory.createConnection();
        connection.setClientID("hxb001");
        connection.start();
        // Session： 一个发送或接收消息的线程
        TopicSession session = (TopicSession) connection.createSession(Boolean.valueOf("false"), Session.AUTO_ACKNOWLEDGE);
        // Destination ：消息的目的地;消息发送给谁.
        // 获取session注意参数值my-queue是Query的名字
        Topic destination = session.createTopic("my-queue");
        // MessageProducer：消息生产者
        TopicSubscriber producer = session.createDurableSubscriber(destination,"hxb");
        // 消费者，消息接收者

        session.close();
        connection.close();
    }
}