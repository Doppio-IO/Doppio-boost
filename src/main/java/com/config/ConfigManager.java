
package javaBullet.config;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class ConfigManager {
    private final Properties config = new Properties();

    public void loadConfig(String filePath) throws IOException {
        try (FileInputStream input = new FileInputStream(filePath)) {
            config.load(input);
        }
    }

    public String getProperty(String key) {
        return config.getProperty(key);
    }
}
