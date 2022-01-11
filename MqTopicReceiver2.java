package cn.knet.mq.mqtest.testing;

import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class MqTopicReceiver2 {
    public static void main(String[] args) throws JMSException {
        // ConnectionFactory ：连接工厂，JMS 用它创建连接
        ConnectionFactory connectionFactory =
                new ActiveMQConnectionFactory("kxwz", "kx.wz123",
                        "tcp://202.173.14.69:61616");
        // JMS 客户端到JMS Provider 的连接
        Connection connection = connectionFactory.createConnection();
        connection.setClientID("001002");
        connection.start();
        // Session： 一个发送或接收消息的线程
        Session session = connection.createSession(Boolean.valueOf("true"), Session.AUTO_ACKNOWLEDGE);
        // Destination ：消息的目的地;消息发送给谁.
        // 获取session注意参数值xingbo.xu-queue是一个服务器的queue，须在在ActiveMq的console配置
        Topic destination = session.createTopic("my-queue");
        // 消费者，消息接收者
        MessageConsumer consumer = session.createDurableSubscriber(destination,"001002003");
        while (true) {
            TextMessage message = (TextMessage) consumer.receive();
            if (null != message) {
                System.out.println("收到消息：" + message.getText());
                session.commit();
            } else {
                break;
            }
        }
        session.close();
        connection.close();
    }
}