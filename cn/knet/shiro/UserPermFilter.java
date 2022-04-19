package cn.knet.seal.shiro;

import org.apache.commons.lang.StringUtils;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.web.filter.authz.AuthorizationFilter;

import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;

/**
 * @author dcx
 * @create 2019-11-28 13:21
 */
public class UserPermFilter extends AuthorizationFilter {

    @Override
    protected boolean isAccessAllowed(ServletRequest request, ServletResponse response, Object mappedValue)
            throws Exception {
        Subject subject = getSubject(request, response);
        HttpServletRequest httpRequest = (HttpServletRequest)request;
        String url = StringUtils.replace(httpRequest.getRequestURI(), "/", ":");
        if (subject.isPermitted(url)) {
            return true;
        }
        return false;
    }
}
