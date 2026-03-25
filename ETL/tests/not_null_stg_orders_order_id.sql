SELECT *
FROM {{ ref('stg_orders') }}
WHERE order_id IS NULL