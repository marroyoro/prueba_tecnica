-- Selecciona la base Gold
USE gold_db;

-- Dimensión de Hoteles
CREATE TABLE gold_dim_hotels AS
SELECT DISTINCT hotel_id,
       hotel_name,
       hotel_category
FROM silver_hotcag;

-- Dimensión de Agencias
CREATE TABLE gold_dim_agencies AS
SELECT DISTINCT agency_id,
       agency_name
FROM silver_hotvta;

-- Dimensión de Clientes
CREATE TABLE gold_dim_clients AS
SELECT DISTINCT c_cve_cxc AS client_id,
       c_nombre AS client_name,
       c_ciudad AS city,
       c_estado AS state,
       c_pais AS country
FROM silver_fact_clients;

-- Dimensión de Tiempo
CREATE TABLE gold_dim_time AS
SELECT DISTINCT DATE(fecha) AS date,
       YEAR(fecha) AS year,
       MONTH(fecha) AS month,
       QUARTER(fecha) AS quarter
FROM silver_fact_clients;

-- Hechos de Reservaciones
CREATE TABLE gold_fact_reservations AS
SELECT r.reservation_id,
       r.hotel_id,
       r.client_id,
       r.agency_id,
       r.fecha,
       r.precio,
       r.estado_reserva
FROM silver_fact_clients r;

-- Hechos de Ventas
CREATE TABLE gold_fact_sales AS
SELECT v.sale_id,
       v.hotel_id,
       v.market_id,
       v.fecha,
       v.ingreso
FROM silver_hotvta v;

-- ADR acumulado por hotel
CREATE VIEW gold_metric_adr AS
SELECT h.hotel_name,
       AVG(r.precio) AS adr_acumulado
FROM gold_fact_reservations r
JOIN gold_dim_hotels h ON r.hotel_id = h.hotel_id
GROUP BY h.hotel_name;

-- Tasa de cancelación por segmento de mercado
CREATE VIEW gold_metric_cancelacion AS
SELECT m.segmento,
       COUNT(CASE WHEN r.estado_reserva = 'cancelada' THEN 1 END) * 1.0 /
       COUNT(*) AS tasa_cancelacion
FROM gold_fact_reservations r
JOIN gold_dim_market m ON r.market_id = m.market_id
GROUP BY m.segmento;

-- Ingresos mensuales
CREATE VIEW gold_metric_ingresos_mensuales AS
SELECT t.year, t.month,
       SUM(s.ingreso) AS ingresos_mensuales
FROM gold_fact_sales s
JOIN gold_dim_time t ON s.fecha = t.date
GROUP BY t.year, t.month
ORDER BY t.year, t.month;