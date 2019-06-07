/*
 * Instituto Tecnologico de Costa Rica
 * Computer Engineering
 * Taller de Programacion
 * 
 * Proyecto Telemetry
 * 
 * Proyecto 2, semestre 1
 * 5/3/2019
 * 
 * Version 1.0.0
 * 
 * Arduino 1.8.9
 * 
 * Profesor: Milton Villegas Lemus.
 * 
 * Autores: Kenneth Fuentes Martinez
 *          Cristian Calvo
 *          
 * Pais de emission: Cosat Rica.
 */
#include <ESP8266WiFi.h>

//Cantidad maxima de clientes es 1
#define MAX_SRV_CLIENTS 1
//Puerto por el que escucha el servidor
#define PORT 7070

/*
 * ssid: Nombre de la Red a la que se va a conectar el Arduino
 * password: Contraseña de la red
 * 
 * Este servidor no funciona correctamente en las redes del TEC,
 * se recomienda crear un hotspot con el celular
 */
const char* ssid = "Tesla";
const char* password = "ac03049700";


// servidor con el puerto y variable con la maxima cantidad de 

WiFiServer server(PORT);
WiFiClient serverClients[MAX_SRV_CLIENTS];

/*
 * Intervalo de tiempo que se espera para comprobar que haya un nuevo mensaje
 */
unsigned long previousMillis = 0, temp = 0;
const long interval = 100;

/*
 * Pin donde está conectado el sensor de luz
 * Señal digital, lee 1 si hay luz y 0 si no hay.
 */
#define ldr D7
/**
 * Variables para manejar las luces con el registro de corrimiento.
 * Utilizan una función propia de Arduino llamada shiftOut.
 * shiftOut(ab,clk,LSBFIRST,data), la función recibe 2 pines, el orden de los bits 
 * y un dato de 8 bits.
 * El registro de corrimiento tiene 8 salidas, desde QA a QH. Nosotros usamos 6 de las 8 salidas
 * Ejemplos al enviar data: 
 * data = B00000000 -> todas encendidas
 * data = B11111111 -> todas apagadas
 * data = B00001111 -> depende de LSBFIRST o MSBFIRST la mitad encendida y la otra mitad apagada
 */
#define ab  D6 
#define clk D8
/*
 * Variables para controlar los motores.
 * EnA y EnB son los que habilitan las salidas del driver.
 * EnA = 0 o EnB = 0 -> free run (No importa que haya en las entradas el motor no recibe potencia)
 * EnA = 0 -> Controla la potencia (Para regular la velocidad utilizar analogWrite(EnA,valor), 
 * con valor [0-1023])
 * EnB = 0 -> Controla la dirección, poner en 0 para avanzar directo.
 * In1 e In2 son inputs de driver, controlan el giro del motor de potencia
 * In1 = 0 ∧ In2 = 1 -> Moverse hacia adelante
 * In1 = 1 ∧ In2 = 0 -> Moverse en reversa
 * In3 e In4 son inputs de driver, controlan la dirección del carro
 * In3 = 0 ∧ In4 = 1 -> Gira hacia la izquierda
 * In3 = 1 ∧ In4 = 0 -> Gira hacia la derecha
 */
#define Bat A0
#define EnA D4 // 
#define In1 D3 // D4 en HIGH : retroceder
#define In2 D2 // D3 en HIGH : avanzar
#define In3 D1 // 
#define EnB D5 // 
#define In4 D0 // 0 para ir hacia adelante

byte data = B11111111;

/**
 * Variables
 */
// #AGREGAR VARIABLES NECESARIAS 

/**
 * Función de configuración.
 * Se ejecuta la primera vez que el módulo se enciende.
 * Si no puede conectarse a la red especificada entra en un ciclo infinito 
 * hasta ser reestablecido y volver a llamar a la función de setup.
 * La velocidad de comunicación serial es de 115200 baudios, tenga presente
 * el valor para el monitor serial.
 */
void setup() {
  Serial.begin(115200);
  pinMode(In1,OUTPUT);
  pinMode(In2,OUTPUT);
  pinMode(In3,OUTPUT);
  pinMode(In4,OUTPUT);
  pinMode(EnA,OUTPUT);
  pinMode(EnB,OUTPUT);
  pinMode(clk,OUTPUT);
  pinMode(ab,OUTPUT);
  pinMode(Bat,INPUT);
  pinMode(ldr,INPUT);

  // ip estática para el servidor
  IPAddress ip(192,168,100,2);
  IPAddress gateway(192,168,100,1);
  IPAddress subnet(255,255,255,0);

  WiFi.config(ip, gateway, subnet);

  // Modo para conectarse a la red
  WiFi.mode(WIFI_STA);
  // Intenta conectar a la red
  WiFi.begin(ssid, password);
  
  uint8_t i = 0;
  while (WiFi.status() != WL_CONNECTED && i++ < 20) delay(500);
  if (i == 21) {
    Serial.print("\nCould not connect to: "); Serial.println(ssid);
    while (1) delay(500);
  } else {
    Serial.print("\nConnection Succeeded to: "); Serial.println(ssid);
    Serial.println(".....\nWaiting for a client at");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
    Serial.print("Port: ");
    Serial.print(PORT);
  }
  server.begin();
  server.setNoDelay(true);

  shiftOut(ab, clk, LSBFIRST, data);


}

/*
 * Función principal que llama a las otras funciones y recibe los mensajes del cliente
 * Esta función comprueba que haya un nuevo mensaje y llama a la función de procesar
 * para interpretar el mensaje recibido.
 */
void loop() {
  
  unsigned long currentMillis = millis();
  uint8_t i;
  //check if there are any new clients
  if (server.hasClient()) {
    for (i = 0; i < MAX_SRV_CLIENTS; i++) {
      //find free/disconnected spot
      if (!serverClients[i] || !serverClients[i].connected()) {
        if (serverClients[i]) serverClients[i].stop();
        serverClients[i] = server.available();
        continue;
      }
    }
    //no free/disconnected spot so reject
    WiFiClient serverClient = server.available();
    serverClient.stop();
  }

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    for (i = 0; i < MAX_SRV_CLIENTS; i++) {
      // El cliente existe y está conectado
      if (serverClients[i] && serverClients[i].connected()) {
        // El cliente tiene un nuevo mensaje
        if(serverClients[i].available()){
          // Leemos el cliente hasta el caracter '\r'
          String mensaje = serverClients[i].readStringUntil('\r');
          // Eliminamos el mensaje leído.
          serverClients[i].flush();
          
          // Preparamos la respuesta para el cliente
          String respuesta; 
          procesar(mensaje, &respuesta);
          Serial.println(mensaje);
          // Escribimos la respuesta al cliente.
          serverClients[i].println(respuesta);
        }  
        serverClients[i].stop();
      }
    }
  }
}

/*
 * Función para dividir los comandos en pares llave, valor
 * para ser interpretados y ejecutados por el Carro
 * Un mensaje puede tener una lista de comandos separados por ;
 * Se analiza cada comando por separado.
 * Esta función es semejante a string.split(char) de python
 * 
 */
void procesar(String input, String * output){
  //Buscamos el delimitador ;
  Serial.println("Checking input....... ");
  int comienzo = 0, delComa, del2puntos;
  bool result = false;
  delComa = input.indexOf(';',comienzo);
  
  while(delComa>0){
    String comando = input.substring(comienzo, delComa);
    Serial.print("Processing comando: ");
    Serial.println(comando);
    del2puntos = comando.indexOf(':');
    /*
    * Si el comando tiene ':', es decir tiene un valor
    * se llama a la función exe 
    */
    if(del2puntos>0){
        String llave = comando.substring(0,del2puntos);
        String valor = comando.substring(del2puntos+1);

        Serial.print("(llave, valor) = ");
        Serial.print(llave);
        Serial.println(valor);
        //Una vez separado en llave valor 
        *output = implementar(llave,valor); 
    }
    else if(comando == "sense"){
      *output = getSense();         
    }

    /**
     * ## AGREGAR COMPARACIONES PARA COMANDOS SIN VALOR
     * EJEM: else if (comando == CIRCLE) {
     *  
     * } 
     */
    else{
      Serial.print("Comando no reconocido. Solo presenta llave");
      *output = "Undefined key value: " + comando+";";
    }
    comienzo = delComa+1;
    delComa = input.indexOf(';',comienzo);
  }
}

String implementar(String llave, String valor){
  /**
   * Funcionamiento: Función que evalua los diferentes comandos que el usuario puede indicar.
   * Entradas:la llave, que sería el nombre del comando y un valor que depende de lo que ejecute cada comando.
   * Salidas: Las salidas se ven reflejadas en el circuito directamente, ya siedo activar o desactivar luces o motores, o ejecutar una accion precostruida.
   * Restriciiones: En pwm debe ser entre -1023 y 1023 para que funcione.
   *                En las demás se evalúa 1 o 0 dependiendo de lo que se hace en cada comando. 
   * 
   */
  String result="ok;";
  Serial.print("Comparing llave: ");
  Serial.println(llave);
  int Valor;
  Valor=valor.toInt();
  
  if(llave == "pwm"){//Ejecuta lo correspondiente al pwm.
    Serial.print("Move....: ");
    Serial.println(valor);
    
    //Código que evalúa si Valor esté entre -1023 y 1023
    //y hace que los motes avancen o retrocedan dependiendo dependiendo de la entrada.
    if (Valor>0 && Valor<=1023){
      digitalWrite(In1, LOW);
      digitalWrite(In2, HIGH);
      analogWrite(EnA, Valor);

      data= data | 0b00110000;
      Serial.println(data);
    }
    else if (Valor<0 && Valor>=-1023){
      digitalWrite(In1, HIGH);
      digitalWrite(In2, LOW);
      analogWrite(EnA, -Valor);

      data= data & 0b11001111;
      Serial.println(data);
    }
    else if(Valor==0){
      digitalWrite(In1, LOW);
      digitalWrite(In2, LOW);
      analogWrite(EnA, 0);

      data= data & 0b11001111;
      Serial.println(data);
      }
    else{
      Serial.println("El valor ingresado debe ser menor que 1023 y mayor que -1023.");
    }
  }
  else if (comando == "ZigZag"){ //Hacer un zigzag
      for (int j=1; j<20; j++){
        digitalWrite(In3, LOW);
        digitalWrite(In4, HIGH);
        analogWrite(EnB, 1023);
        for(int i=1; i<10; i++){
          digitalWrite(In1, HIGH);
          digitalWrite(In2, LOW);
          analogWrite(EnA, 700);
          delay(400);
        }
        digitalWrite(In3, HIGH);
        digitalWrite(In4, LOW);
        analogWrite(EnB, 1023);
        for(int i=1; i<10; i++){
          digitalWrite(In1, HIGH);
          digitalWrite(In2, LOW);
          analogWrite(EnA, 700);
          delay(400);
        }
     }
  }
  else if(llave=="Circle"){//Comando que hace un círculo.
    if(valor.toInt()==1){//Se evaluan casos para ver hacia qué lado se hace el círculo.
  data= data | 0b00110000;
  Serial.println(data);
  
  digitalWrite(In3, LOW);
  digitalWrite(In4, HIGH);
  analogWrite(EnB, 1023);

  digitalWrite(In1, LOW);
  digitalWrite(In2, HIGH);
  analogWrite(EnA, 900);

  delay(20000);

  digitalWrite(In3, LOW);
  digitalWrite(In4, LOW);
  analogWrite(EnB, 0);

  digitalWrite(In1, LOW);
  digitalWrite(In2, LOW);
  analogWrite(EnA, 0);

  data= data & 0b11001111;
  Serial.println(data);
    }
    else if(valor.toInt()==-1){
  data= data | 0b00110000;
  Serial.println(data);
  
  digitalWrite(In3, HIGH);
  digitalWrite(In4, LOW);
  analogWrite(EnB, 1023);

  digitalWrite(In1, LOW);
  digitalWrite(In2, HIGH);
  analogWrite(EnA, 900);

  delay(20000);

  digitalWrite(In3, LOW);
  digitalWrite(In4, LOW);
  analogWrite(EnB, 0);

  digitalWrite(In1, LOW);
  digitalWrite(In2, LOW);
  analogWrite(EnA, 0);

  data= data & 0b11001111;
  Serial.println(data);
  
    }
    else{
      return " ";
    }
    
  }
  else if(llave=="Infinite"){//Hace una figura tipo un ocho invertido.
    switch (valor.toInt()){
      
    case 1:{//Evalua solo el caso 1 para iniciar el comando.
  data= data | 0b00110000;
  Serial.println(data);
      
  digitalWrite(In3, LOW);
  digitalWrite(In4, HIGH);
  analogWrite(EnB, 1023);

  digitalWrite(In1, LOW);
  digitalWrite(In2, HIGH);
  analogWrite(EnA, 900);

  delay(20000);

  digitalWrite(In3, HIGH);
  digitalWrite(In4, LOW);
  analogWrite(EnB, 1023);

  digitalWrite(In1, LOW);
  digitalWrite(In2, HIGH);
  analogWrite(EnA, 900);

  delay(20000);

  digitalWrite(In3, LOW);
  digitalWrite(In4, LOW);
  analogWrite(EnB, 0);

  digitalWrite(In1, LOW);
  digitalWrite(In2, LOW);
  analogWrite(EnA, 0);

  data= data & 0b11001111;
  Serial.println(data);
    }
    break;
    default:{
      return "";
    }
    break;
    }
  }
  else if (comando == "Especial"){ //Se parquea
    digitalWrite(In3, LOW);
    digitalWrite(In4, HIGH);
    analogWrite(EnB, 1023);

    for(int i=1; i<15; i++){ 
      digitalWrite(In1, HIGH);
      digitalWrite(In2, LOW);
      analogWrite(EnA, 700);
      delay(400);
    }
    digitalWrite(In3, LOW);
    digitalWrite(In4, LOW);
    analogWrite(EnB, 0);
    for(int j=1; j<15; j++){
      digitalWrite(In1, LOW);
      digitalWrite(In2, HIGH);
      analogWrite(EnA, 700);
    }
    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    analogWrite(EnA, 0);
  }
  else{
    Serial.print("Comando no reconocido. Solo presenta llave");
    *output = "Undefined key value: " + comando+";";
  }
  comienzo = delComa+1;
  delComa = input.indexOf(';',comienzo);
  }
}
  else if(llave == "dir"){//Comando que hace girar el carrito.
    switch (valor.toInt()){
      case 1:
        Serial.println("Girando derecha");
        //Gira hacia la derecha.
        {
      digitalWrite(In3, LOW);
      digitalWrite(In4, HIGH);
      analogWrite(EnB, 1023);
      }
        break;
      case -1:
        Serial.println("Girando izquierda");
        //Gira hacia la izquierda.
        {
      digitalWrite(In3, HIGH);
      digitalWrite(In4, LOW);
      analogWrite(EnB, 1023);
      }
        break;
       default:
        Serial.println("directo");
        // No gira. 
        {
      digitalWrite(In3, LOW);
      digitalWrite(In4, LOW);
      analogWrite(EnB, 0);
      }
        break;
    }
  }
  else if(llave[0] == 'l'){//Comando que hace cambiar las luces de diferentes tipos.
    Serial.println("Cambiando Luces");
    Serial.print("valor luz: ");
    Serial.println(valor);
    //
    switch (llave[1]){//Se utilizan bitwise operators para poder cambiar la variable data que guarda los bits para el registro de corrimiento.
      case 'f':
        Serial.println("Luces frontales");
        if (valor=="0"){
            data= data | 0b00001100;
            Serial.println(data);
        }
        else if (valor=="1"){
            data= data & 0b11110011;
            Serial.println(data);
          }
        break;
      case 'b':
        Serial.println("Luces traseras");
       
        if (valor=="0"){
            data= data | 0b00110000;
            Serial.println(data);
        }
        else if (valor=="1"){
            data= data & 0b11001111;
            Serial.println(data);
          }
        break;
      case 'l':
        Serial.println("Luces izquierda");

        if (valor=="0"){
            data= data | 0b10000000;
            Serial.println(data);
        }
        else if (valor=="1"){
            data= data & 0b01111111;
            Serial.println(data);
          }
        break;
      case 'r':
        Serial.println("Luces derechas");
       
         if (valor=="0"){
            data= data | 0b01000000;
            Serial.println(data);
        }
        else if (valor=="1"){
            data= data & 0b10111111;
            Serial.println(data);
          }
        break;

      default:
        Serial.println("Ninguna de las anteriores");
        
        break;
    }

  }

  else{
    result = "Undefined key value: " + llave+";";
    Serial.println(result);
  }
  shiftOut(ab, clk, LSBFIRST, data);//Acá se actualizan las luces.
  return result;
}

/**
 * Función para obtener los valores de telemetría del auto
 */
String getSense(){
  //Código donde se obtienen valores correpondientes a salidas analógicas y digitales.
  int batteryLvl = map(analogRead(Bat),0,1023,10,100);//Lectura del pin A0 para determinar el porcentaje de la batería.
  int light = digitalRead(ldr);//Lectura del pin D7 para el nivel de luz.

  // EQUIVALENTE A UTILIZAR STR.FORMAT EN PYTHON, %d -> valor decimal
  char sense [16];
  sprintf(sense, "blvl:%d;ldr:%d;", batteryLvl, light);
  Serial.print("Sensing: ");
  Serial.println(sense);
  return sense;
}
