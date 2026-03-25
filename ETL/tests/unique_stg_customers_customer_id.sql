SELECT customer_id, COUNT(*) as nb
FROM {{ ref('stg_customers') }}
GROUP BY customer_id
HAVING COUNT(*) > 1