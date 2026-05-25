// mqtt_subscriber.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mosquitto.h>
#include <mysql.h> // Ruta estándar en distribuciones Linux modernas
#include <json.h>

#define TOPIC "sensor/dht"
#define BROKER "10.42.0.117" // IP remota de tu Raspberry Pi
#define PORT 1883
#define MOSQoS 1

MYSQL *conn;

void insertar_datos(const char *timestamp, float temp, float hum) {
    char query[512];
    snprintf(query, sizeof(query),
             "INSERT INTO dht_data (timestamp, temperatura, humedad) VALUES ('%s', %.2f, %.2f)",
             timestamp, temp, hum);
             
    if (mysql_query(conn, query)) {
        fprintf(stderr, "❌ [MariaDB] Error al insertar: %s\n", mysql_error(conn));
    } else {
        printf("💾 [MariaDB] Registro almacenado exitosamente.\n");
    }
    fflush(stdout);
}

void on_message(struct mosquitto *mosq, void *userdata, const struct mosquitto_message *msg) {
    if (msg->payloadlen) {
        struct json_object *jroot = json_tokener_parse(msg->payload);
        struct json_object *jts, *jtemp, *jhum;
        
        if (json_object_object_get_ex(jroot, "timestamp", &jts) &&
            json_object_object_get_ex(jroot, "temperatura", &jtemp) &&
            json_object_object_get_ex(jroot, "humedad", &jhum)) {
            
            printf("📥 Mensaje MQTT Recibido: %s\n", (char *)msg->payload);
            insertar_datos(json_object_get_string(jts),
                           json_object_get_double(jtemp),
                           json_object_get_double(jhum));
        }
        json_object_put(jroot); // Liberar memoria del objeto JSON
    }
}

int main() {
    // Inicialización de conexión a Base de Datos MariaDB local en tu PC
    conn = mysql_init(NULL);
    if (!mysql_real_connect(conn, "localhost", "root", "root", "sensores", 0, NULL, 0)) {
        fprintf(stderr, "❌ Error al conectar a MariaDB: %s\n", mysql_error(conn));
        return 1;
    }
    printf("🔗 Conectado exitosamente a MariaDB (Base de datos: sensores).\n");

    mosquitto_lib_init();
    struct mosquitto *mosq = mosquitto_new("subscriptor_dht", false, NULL);
    
    mosquitto_message_callback_set(mosq, on_message);
    
    printf("📡 Conectando al broker en %s...\n", BROKER);
    if (mosquitto_connect(mosq, BROKER, PORT, 60) != MOSQ_ERR_SUCCESS) {
        fprintf(stderr, "❌ No se pudo conectar al Broker MQTT.\n");
        return 1;
    }

    mosquitto_subscribe(mosq, NULL, TOPIC, MOSQoS);
    printf("🤖 Suscriptor en C listo. Esperando transmisiones...\n");
    fflush(stdout);

    mosquitto_loop_forever(mosq, -1, 1);

    mosquitto_destroy(mosq);
    mosquitto_lib_cleanup();
    mysql_close(conn);
    return 0;
}
