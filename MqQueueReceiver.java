package cn.knet.mq.mqtest.testing;

import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class MqQueueReceiver {
    public static void main(String[] args) throws JMSException {
        // ConnectionFactory ：连接工厂，JMS 用它创建连接
        ConnectionFactory connectionFactory =
                new ActiveMQConnectionFactory("kxwz", "kx.wz123",
                        "tcp://202.173.14.69:61616");
        // JMS 客户端到JMS Provider 的连接
        Connection connection = connectionFactory.createConnection();
        // Session： 一个发送或接收消息的线程
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        // Destination ：消息的目的地;消息发送给谁.
        // 获取session注意参数值xingbo.xu-queue是一个服务器的queue，须在在ActiveMq的console配置
        Destination destination = session.createQueue("my-queue");
        // 消费者，消息接收者
        MessageConsumer consumer = session.createConsumer(destination);
        connection.start();
        /**
         * 接收方法一：
         */
//        while (true) {
//            TextMessage message = (TextMessage) consumer.receive();
//            if (null != message) {
//                System.out.println("收到消息：" + message.getText());
////                session.commit();
//            } else {
//                break;
//            }
//        }
        /**
         * 接收方法二：
         */
        // 消息消费者接收消息
        consumer.setMessageListener(new MessageListener() {
            //当我们监听的topic 中存在消息 这个方法自动执行
            public void onMessage(Message message) {
                //判断消息是否为空并且是否是TextMessage类型
                if (message != null && message instanceof TextMessage) {
                    TextMessage textMessage = (TextMessage) message;
                    try {
                        System.out.println("消费者接收到了消息：" + textMessage.getText());
                    } catch (JMSException e) {
                        e.printStackTrace();
                    }
                }
            }
        });
//        consumer.close();
//        session.close();
//        connection.close();
    }
}