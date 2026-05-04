# medallon_dbt_airflow
Implementación de una arquitectura medallion completa (Bronze, Silver, Gold) usando dbt para transformaciones y Airflow para orquestación sobre un warehouse en Postgres.

# Medallion Architecture Project (dbt + Airflow + Postgres)

## Arquitectura
Bronze → Silver → Gold

## Stack
- Airflow (orquestación)
- dbt (transformación)
- Postgres (warehouse)
- Docker

## Flujo
1. Bronze: ingesta datos crudos
2. Silver: limpieza
3. Gold: métricas de negocio

## Ejecutar

docker-compose up -d

Airflow: http://localhost:8080

## DAG
medallion_pipeline

## Resultado
Tabla final: fact_user_spending
--contiene un ejemplo del result doc_como_correr.txt

