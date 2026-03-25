SELECT order_id, COUNT(*) as nb
FROM {{ ref('stg_orders') }}
GROUP BY order_id
HAVING COUNT(*) > 1