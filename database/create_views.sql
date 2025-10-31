CREATE OR ALTER VIEW dbo.vw_listing_features
AS
WITH cal AS (
    SELECT
        listing_id,
        COUNT(*) AS total_weeks,
        SUM(CASE WHEN available_days_per_week = 0 THEN 1 ELSE 0 END) AS offline_weeks,
        AVG(CAST(available_days_per_week AS FLOAT)) AS mean_availability,
        MIN(week_start_date) AS first_week,
        MAX(week_start_date) AS last_week
    FROM dbo.fact_calendar
    GROUP BY listing_id
)
SELECT
    c.listing_id,
    c.total_weeks,
    c.offline_weeks,
    CASE WHEN c.total_weeks = 0 THEN 0 ELSE 1.0 * c.offline_weeks / c.total_weeks END AS pct_offline_weeks,
    c.mean_availability,
    c.first_week,
    c.last_week,
    dl.price AS base_price,
    dl.number_of_reviews,
    dl.property_city,
    dl.property_country,
    dl.property_neighbourhood,
    dl.latitude,
    dl.longitude,
    dl.host_id,
    dl.host_name,
    dl.review_scores_rating
FROM cal c
LEFT JOIN dbo.dim_listings dl ON dl.listing_id = c.listing_id;
