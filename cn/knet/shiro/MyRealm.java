package cn.knet.seal.shiro;


import cn.knet.seal.entity.KnetPermission;
import cn.knet.seal.entity.KnetUser;
import cn.knet.seal.enums.StatusEnum;
import cn.knet.seal.mapper.KnetPermissionMapper;
import cn.knet.seal.mapper.KnetUserMapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.apache.shiro.authc.*;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.DigestUtils;

import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.Charset;
import java.util.List;

/**
 * @author dcx
 * @create 2019-11-25 10:30
 */
@Service
public class MyRealm extends AuthorizingRealm {
    private static final Logger logger = LoggerFactory.getLogger(AuthorizingRealm.class);
    @Autowired
    KnetUserMapper knetUserMapper;
    @Autowired
    KnetPermissionMapper knetPermissionMapper;

    /**
     * 只有当需要检测用户权限的时候才会调用此方法
     */
    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principals) {
        logger.info("method[doGetAuthorizationInfo] begin.");
        KnetUser user = (KnetUser) principals.fromRealm(getName()).iterator().next();
        SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();
        if (user != null) {
            try {
                List<KnetPermission> l = knetPermissionMapper.selectALlPermissionList(user.getId());
                if (l != null && l.size() > 0) {
                    for (KnetPermission kp : l) {
                        logger.info("method[doGetAuthorizationInfo] add perm<" + kp.getPerm() + ">");
                        info.addStringPermission(kp.getPerm());
                    }
                }
                return info;
            } catch (Exception e) {
                logger.error("method[doGetAuthorizationInfo] e.message<" + e.getMessage() + "> e<" + e + ">", e);
            }
        }
        return null;
    }

    /**
     * 默认使用此方法进行用户名正确与否验证，错误抛出异常即可。
     */
    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken auth) throws AuthenticationException {
        UsernamePasswordToken token = (UsernamePasswordToken) auth;
        byte[] bytes = getBytes(token.getPassword());
        List<KnetUser> list = knetUserMapper.selectList(new QueryWrapper<KnetUser>().eq("USERNAME", token.getUsername())
                .eq("PASSWORD", DigestUtils.md5DigestAsHex(bytes))
                .eq("STATUS", StatusEnum.ABLE));
        if (list != null && list.size() > 0) {
            return new SimpleAuthenticationInfo(list.get(0), token.getPassword(), getName());
        }
        throw new AuthenticationException("用户名密码错误");
    }

    public static byte[] getBytes(char[] chars) {
        Charset cs = Charset.forName("UTF-8");
        CharBuffer cb = CharBuffer.allocate(chars.length);
        cb.put(chars);
        cb.flip();
        ByteBuffer bb = cs.encode(cb);
        return bb.array();
    }
}
