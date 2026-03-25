SELECT *
FROM {{ ref('stg_customers') }}
WHERE customer_name IS NULL