
package javaBullet.memory;

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
