SELECT
    user_id,
    SUM(amount) AS total_spent
FROM {{ ref('stg_events') }}
WHERE event_type = 'purchase'
GROUP BY user_id