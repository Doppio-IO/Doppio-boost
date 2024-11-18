# Vamos criar a estrutura de projeto Maven básica com as dependências e classes solicitadas.
import os
import zipfile

# Diretório base do projeto
project_name = "javaBullet"
base_dir = f"/mnt/data/{project_name}"
src_main_java = os.path.join(base_dir, "src/main/java/com/javabullet")
src_main_resources = os.path.join(base_dir, "src/main/resources")
src_test_java = os.path.join(base_dir, "src/test/java/com/javabullet")

# Criar estrutura de diretórios
os.makedirs(src_main_java, exist_ok=True)
os.makedirs(src_main_resources, exist_ok=True)
os.makedirs(src_test_java, exist_ok=True)

# Criar o arquivo pom.xml com dependências
pom_content = """<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.javabullet</groupId>
    <artifactId>javaBullet</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <!-- Caffeine Cache -->
        <dependency>
            <groupId>com.github.ben-manes.caffeine</groupId>
            <artifactId>caffeine</artifactId>
            <version>3.1.8</version>
        </dependency>
        <!-- Apache Commons Lang -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-lang3</artifactId>
            <version>3.12.0</version>
        </dependency>
        <!-- SLF4J for Logging -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>2.0.9</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-simple</artifactId>
            <version>2.0.9</version>
        </dependency>
    </dependencies>
</project>
"""

with open(os.path.join(base_dir, "pom.xml"), "w") as pom_file:
    pom_file.write(pom_content)

# Criar classes iniciais no src/main/java
object_pool_code = """package com.javabullet.memory;

import java.util.LinkedList;
import java.util.Queue;
import java.util.function.Supplier;

public class ObjectPool<T> {
    private final Queue<T> pool = new LinkedList<>();
    private final Supplier<T> objectFactory;

    public ObjectPool(Supplier<T> factory, int initialSize) {
        this.objectFactory = factory;
        for (int i = 0; i < initialSize; i++) {
            pool.add(factory.get());
        }
    }

    public T borrowObject() {
        return pool.isEmpty() ? objectFactory.get() : pool.poll();
    }

    public void returnObject(T obj) {
        pool.offer(obj);
    }
}
"""

cache_code = """package com.javabullet.cache;

import com.github.benmanes.caffeine.cache.Cache;
import com.github.benmanes.caffeine.cache.Caffeine;

import java.util.concurrent.TimeUnit;

public class CacheManager<K, V> {
    private final Cache<K, V> cache;

    public CacheManager(long maxSize, long expireAfterMinutes) {
        this.cache = Caffeine.newBuilder()
                .maximumSize(maxSize)
                .expireAfterAccess(expireAfterMinutes, TimeUnit.MINUTES)
                .build();
    }

    public void put(K key, V value) {
        cache.put(key, value);
    }

    public V get(K key) {
        return cache.getIfPresent(key);
    }

    public void invalidate(K key) {
        cache.invalidate(key);
    }
}
"""

config_manager_code = """package com.javabullet.config;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class ConfigManager {
    private final Properties properties = new Properties();

    public void loadConfig(String filePath) throws IOException {
        try (FileInputStream input = new FileInputStream(filePath)) {
            properties.load(input);
        }
    }

    public String getProperty(String key) {
        return properties.getProperty(key);
    }
}
"""

with open(os.path.join(src_main_java, "memory/ObjectPool.java"), "w") as pool_file:
    pool_file.write(object_pool_code)

with open(os.path.join(src_main_java, "cache/CacheManager.java"), "w") as cache_file:
    cache_file.write(cache_code)

with open(os.path.join(src_main_java, "config/ConfigManager.java"), "w") as config_file:
    config_file.write(config_manager_code)

config_example = """# Configuração do javaBullet
cache.maxSize=100
cache.expireAfterMinutes=10
"""
with open(os.path.join(src_main_resources, "application.properties"), "w") as config_file:
    config_file.write(config_example)

zip_path = f"/mnt/data/{project_name}.zip"
with zipfile.ZipFile(zip_path, 'w') as project_zip:
    for foldername, subfolders, filenames in os.walk(base_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, base_dir)
            project_zip.write(file_path, arcname)

zip_path