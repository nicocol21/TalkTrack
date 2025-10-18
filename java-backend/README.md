# Java backend (Spring Boot) para TalkTrack

Requisitos:
- JDK 17+
- Maven

Ejecutar en desarrollo:

```powershell
cd java-backend
mvn spring-boot:run
```

O compilar y ejecutar el JAR:

```powershell
cd java-backend
mvn package
java -jar target/java-backend-0.0.1-SNAPSHOT.jar
```

El servidor arrancará en http://localhost:8081/ (configurado en application.properties).
