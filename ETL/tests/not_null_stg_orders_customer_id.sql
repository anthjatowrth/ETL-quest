SELECT *
FROM {{ ref('stg_orders') }}
WHERE customer_id IS NULL