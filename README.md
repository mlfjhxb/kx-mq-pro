package cn.knet.excel.imp.knetexceltool.task;

import cn.knet.excel.imp.knetexceltool.comm.KnetBgdataCommonInit;
import cn.knet.excel.imp.knetexceltool.service.KnetBgdataCompanyBaseService;
import cn.knet.excel.imp.knetexceltool.thread.KnetBgdataFilterThread;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.LongAdder;

/**
 *
 */
@Service
@Slf4j
public class KnetBgdataCleanTask extends KnetBgdataCommonInit {

    @Resource
    private KnetBgdataCompanyBaseService knetBgdataCompanyBaseService;

   @Scheduled(cron = "${task.bgdata.clean}")
    public void startFilter() throws Exception {
        /**
         *初始化相关数据 省市县、剔除词
         */
        initing();
        /**
         * 定义计数器
         */
        LongAdder rowStarAdder = new LongAdder();
        LongAdder queryCntAdder = new LongAdder();
        LongAdder kwOkAdder = new LongAdder();
        LongAdder kwErrorAdder = new LongAdder();

        log.info(String.format("====beginning to clean bgdata ===="));
        long stime = System.currentTimeMillis();
        /**
         * 分页从mysql中提取数据，分给多线程处理
         */
        int totalSize = knetBgdataCompanyBaseService.selectBgdataSmtCount();
        int pageSize = 5000;
        int cycle = totalSize % pageSize > 0 ? totalSize / pageSize + 1 : totalSize / pageSize;
        int startNum = 0;
        log.info("******* total size from db is [{}]  cytle[{}] *******", totalSize,cycle);
        ExecutorService exector = Executors.newFixedThreadPool(10);
        for (int i = 1; i <= cycle; i++) {
            exector.submit(new KnetBgdataFilterThread(startNum, rowStarAdder, queryCntAdder, kwOkAdder, kwErrorAdder, knetBgdataCompanyBaseService, pageSize));
            startNum += pageSize;
        }
        exector.shutdown();
        //保证任务全部执行完
        while (!exector.awaitTermination(10, TimeUnit.MINUTES)) {
            System.out.println("**** please wait,in importing.... ****");
        }
        long etime = System.currentTimeMillis();
        log.info(String.format("====ending to clean bgdata ==== query_kwok_kwerr size[%s_%s_%s] total_tim[%s]秒", queryCntAdder.sum(), kwOkAdder.sum(), kwErrorAdder.sum(), (etime - stime) / 1000d));
    }


}
