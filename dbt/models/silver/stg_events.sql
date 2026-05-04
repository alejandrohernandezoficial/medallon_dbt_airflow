SELECT
        user_id,
        event_type,
        amount
   FROM {{ ref('raw_events') }}     
WHERE user_id IS NOT NULL