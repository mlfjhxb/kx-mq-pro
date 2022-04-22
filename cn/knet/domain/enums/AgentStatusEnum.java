package cn.knet.domain.enums;

import com.fasterxml.jackson.annotation.JsonValue;

import java.lang.reflect.Field;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

public enum AgentStatusEnum {

    UNPASS("UNPASS", "审核不通过"), AUDITING("AUDITING", "审核中"), OK("OK", "正常"), CLOSE("CLOSE", "关闭");

    private static final Map<String, String> MAPPING = new LinkedHashMap<String, String>();

    private static final Map<String, String> INVERSE_MAPPING = new LinkedHashMap<String, String>();
    @ToJson
    private String value;
    @ToJson
    private String text;

    AgentStatusEnum(final String value, final String text) {
        this.value = value;
        this.text = text;
    }

    static {
        for (AgentStatusEnum em : AgentStatusEnum.values()) {
            MAPPING.put(em.getText(), em.getValue());
            INVERSE_MAPPING.put(em.getValue(), em.getText());
        }
    }

    public String getValue() {
        return value;
    }

    public String getText() {
        return text;
    }

    /**
     * @return
     */
    public static Map<String, String> mapping() {
        return MAPPING;
    }

    /**
     * @return
     */
    public static Map<String, String> inverseMapping() {
        return INVERSE_MAPPING;
    }

    @JsonValue
    public Map<String, Object> jsonValue() throws IllegalArgumentException,
            IllegalAccessException {
        Map<String, Object> map = new HashMap<String, Object>();
        Field[] fields = getClass().getDeclaredFields();
        for (Field f : fields) {
            ToJson toJson = f.getAnnotation(ToJson.class);
            if (toJson != null) {
                f.setAccessible(true);
                Object v = f.get(this);
                map.put(f.getName(), v);
            }
        }
        return map;
    }

}
