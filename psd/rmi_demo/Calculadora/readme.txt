* para compilar cliente:
javac ClienteCalculadora.java 
* para rodar cliente:
java ClienteCalculadora

* para compilar servidor:
javac -Djava.rmi.server.hostname=<ip_da_maquina> ServidorCalculadora
* para rodar servidor:
java ServidorCalculadora