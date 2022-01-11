package cn.knet.mq.mqtest.testing;

import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class TopicPersistentReceiver {
    public static void main(String[] args) throws Exception {
        TopicPersistentReceiver obj = new TopicPersistentReceiver();
        obj.receive();
    }

    //编写消息的接收方---消息的消费者

    public void receive() throws Exception {
        //创建连接工厂对象
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("kxwz", "kx.wz123",
                "tcp://202.173.14.69:61616");
        //从工厂中获取连接对象
        Connection connection = connectionFactory.createConnection();
        //设置客户端id
        connection.setClientID("client-1");
        //连接MQ服务
        connection.start();
        //获得回话（session）对象
        final Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        //通过session对象创建Topic
        Topic topic = session.createTopic("itheimaTopic");
        //通过session对象创建消息的消费者
        //MessageConsumer consumer = session.createConsumer(topic);
        //客户端持久化订阅
        TopicSubscriber consumer = session.createDurableSubscriber(topic, "client1");
        //指定消息监听器
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
        //消息消费者 要时刻在线 连接对象 会话对象均不需要关闭
        //模拟web场景当执行结束后不能让线程结束
        while (true) {
            //死循环  不让消费者线程停掉
        }
    }
}
