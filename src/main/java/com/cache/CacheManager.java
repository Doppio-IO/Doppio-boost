
package javaBullet.cache;

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
