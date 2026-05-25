// cliente_c.c
#include <stdio.h>
#include <stdlib.h>
#include <mosquitto.h>

// Callback que se activa cuando llega un mensaje del broker
void mensaje_callback(struct mosquitto *mosq, void *userdata, const struct mosquitto_message *msg) {
    printf("Mensaje recibido en tópico '%s': %s\n", msg->topic, (char *)msg->payload);
    fflush(stdout); // Limpia el búfer para mostrar el texto de inmediato
}

int main() {
    int rc;
    // CONFIGURACIÓN: Pon la misma IP de la Raspberry Pi
    const char *broker_ip = "10.42.0.117"; 

    mosquitto_lib_init();
    
    struct mosquitto *mosq = mosquitto_new("ClienteC", true, NULL);
    if (!mosq) {
        fprintf(stderr, "Error al crear el cliente.\n");
        return 1;
    }
    
    mosquitto_message_callback_set(mosq, mensaje_callback);
    
    printf("Conectando al broker en %s...\n", broker_ip);
    fflush(stdout);

    rc = mosquitto_connect(mosq, broker_ip, 1883, 60);
    if (rc != MOSQ_ERR_SUCCESS) {
        fprintf(stderr, "No se pudo conectar: %s\n", mosquitto_strerror(rc));
        return 1;
    }
    
    // Suscripción al tópico con QoS 0
    mosquitto_subscribe(mosq, NULL, "iot/temperatura", 0);
    printf("Suscrito exitosamente. Esperando datos...\n");
    fflush(stdout);

    // Bucle infinito de escucha
    mosquitto_loop_forever(mosq, -1, 1);
    
    mosquitto_destroy(mosq);
    mosquitto_lib_cleanup();
    return 0;
}
