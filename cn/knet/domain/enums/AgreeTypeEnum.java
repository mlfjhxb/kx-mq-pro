package cn.knet.domain.enums;

import com.fasterxml.jackson.annotation.JsonValue;

import java.lang.reflect.Field;
import java.util.HashMap;
import java.util.Map;

public enum AgreeTypeEnum {
    ADD("ADD", "补充协议"),
    STANDARD("STANDARD", "标准协议");

    private AgreeTypeEnum(String value, String text) {
        this.value = value;
        this.text = text;
    }

    @ToJson
    String value;
    @ToJson
    String text;

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    @JsonValue
    public Map<String, Object> jsonValue() throws IllegalArgumentException, IllegalAccessException {
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
