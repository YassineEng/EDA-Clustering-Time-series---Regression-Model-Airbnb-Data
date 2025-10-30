CREATE OR ALTER VIEW dbo.vw_listing_features
AS
WITH cal AS (
    SELECT
        listing_id,
        COUNT(*) AS total_weeks,
        SUM(CASE WHEN avg_price_per_week IS NOT NULL THEN 1 ELSE 0 END) AS weeks_with_price,
        AVG(CAST(avg_price_per_week AS FLOAT)) AS mean_weekly_price,
        STDEV(CAST(avg_price_per_week AS FLOAT)) AS std_weekly_price,
        MIN(CAST(avg_price_per_week AS FLOAT)) AS min_weekly_price,
        MAX(CAST(avg_price_per_week AS FLOAT)) AS max_weekly_price,
        AVG(CAST(available_days_per_week AS FLOAT)) AS mean_availability,
        SUM(CASE WHEN available_days_per_week = 0 THEN 1 ELSE 0 END) AS offline_weeks,
        MIN(week_start_date) AS first_week,
        MAX(week_start_date) AS last_week
    FROM dbo.fact_calendar
    GROUP BY listing_id
),
rev AS (
    SELECT
        listing_id,
        COUNT(*) AS review_count
    FROM dbo.fact_reviews
    GROUP BY listing_id
)
SELECT
    c.listing_id,
    c.total_weeks,
    c.weeks_with_price,
    CASE WHEN c.total_weeks = 0 THEN 0 ELSE 1.0 * c.weeks_with_price / c.total_weeks END AS pct_weeks_with_price,
    c.mean_weekly_price,
    c.std_weekly_price,
    c.min_weekly_price,
    c.max_weekly_price,
    c.mean_availability,
    c.offline_weeks,
    CASE WHEN c.total_weeks = 0 THEN 0 ELSE 1.0 * c.offline_weeks / c.total_weeks END AS pct_offline_weeks,
    c.first_week,
    c.last_week,
    dl.price AS base_price,
    dl.number_of_reviews,
    dl.review_scores_rating,
    dl.property_city,
    dl.property_country,
    dl.property_neighbourhood,
    dl.latitude,
    dl.longitude,
    dl.host_id,
    dl.host_name,
    r.review_count AS review_count_fact
FROM cal c
LEFT JOIN dbo.dim_listings dl ON dl.listing_id = c.listing_id
LEFT JOIN rev r ON r.listing_id = c.listing_id;
