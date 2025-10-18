@echo off
cd %~dp0
if not exist mvnw (
  mvn spring-boot:run
) else (
  call mvnw spring-boot:run
)
