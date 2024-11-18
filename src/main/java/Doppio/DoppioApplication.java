package Doppio;

import com.Doppio.Cache.CacheManager;
import com.Doppio.ConfigManager;
import com.Doppio.memory.ObjectPool;
import com.Doppio.monitoring.MetricsCollector;

public class DoppioApplication {

    public static void main(String[] args) {
        System.out.println("Iniciando o Doppio Framework...");

// Exemplo de uso de Object Pooling 
        ObjectPool<String> stringPool = new ObjectPool<>(() -> new String("Objeto Reutilizado"), 10);
        String obj = stringPool.borrowObject();
        System.out.println("Objeto emprestado do pool: " + obj);
        stringPool.returnObject(obj);
        System.out.println("Objeto retornado ao pool");

// Exemplo de uso de Cache
        CacheManager<String, Integer> cache = new CacheManager<>();
        cache.put("ChaveExemplo", 123);
        System.out.println("Valor do cache para 'ChaveExemplo': " + cache.get("ChaveExemplo"));

// Exemplo de uso do Monitoramento de Métricas
        MetricsCollector collector = new MetricsCollector();
        collector.increment("exemploMetric");
        System.out.println("Métrica 'exemploMetric': " + collector.getMetric("exemploMetric"));

// Exemplo de carregamento de configuração
        ConfigManager configManager = new ConfigManager();
        try {
            configManager.loadConfig("config.properties");
            System.out.println("Configuração carregada com sucesso!");
        } catch (Exception e) {
            System.out.println("Erro ao carregar a configuração: " + e.getMessage());
        }

        System.out.println("Doppio Framework iniciado com sucesso!");
    }
}