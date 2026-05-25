// cliente_qos.c
#include <stdio.h>
#include <stdlib.h>
#include <mosquitto.h>

// Función Callback: Se ejecuta automáticamente al recibir un mensaje
void mensaje_callback(struct mosquitto *mosq, void *userdata, const struct mosquitto_message *msg) {
    printf("Recibido [%s]: %s (QoS de entrega: %d)\n", msg->topic, (char *)msg->payload, msg->qos);
    // Forzar a la terminal de Linux a vaciar el búfer para mostrar el texto al instante
    fflush(stdout); 
}

int main() {
    int qos = 1; // Cambia entre 0, 1 o 2 para tus experimentos
    int rc;
    const char *broker_ip = "10.42.0.117"; // IP de la Raspberry Pi

    mosquitto_lib_init();
    
    struct mosquitto *mosq = mosquitto_new("ClienteQoSC", true, NULL);
    if (!mosq) {
        fprintf(stderr, "Error al crear el cliente.\n");
        fflush(stderr);
        return 1;
    }

    mosquitto_message_callback_set(mosq, mensaje_callback);
    
    printf("Conectando al broker en la IP %s...\n", broker_ip);
    fflush(stdout);

    // Conexión directa a la dirección IP de la Raspberry Pi
    rc = mosquitto_connect(mosq, broker_ip, 1883, 60);
    if (rc != MOSQ_ERR_SUCCESS) {
        fprintf(stderr, "Error de conexión: %s\n", mosquitto_strerror(rc));
        fflush(stderr);
        mosquitto_destroy(mosq);
        mosquitto_lib_cleanup();
        return 1;
    }

    printf("¡Conectado exitosamente al broker!\n");
    fflush(stdout);

    // Suscripción al topic con el QoS definido
    rc = mosquitto_subscribe(mosq, NULL, "iot/qos/temp", qos);
    if (rc != MOSQ_ERR_SUCCESS) {
        fprintf(stderr, "Error al suscribirse: %s\n", mosquitto_strerror(rc));
        fflush(stderr);
        mosquitto_destroy(mosq);
        mosquitto_lib_cleanup();
        return 1;
    }

    printf("Suscrito al topic 'iot/qos/temp' con QoS %d. Esperando mensajes...\n", qos);
    fflush(stdout);

    // Bucle infinito para escuchar la red de manera permanente con reconexión automática
    mosquitto_loop_forever(mosq, -1, 1);

    mosquitto_destroy(mosq);
    mosquitto_lib_cleanup();

    return 0;
}
