-- Drop the table if it already exists
IF OBJECT_ID('dbo.listing_features', 'U') IS NOT NULL
    DROP TABLE dbo.listing_features;

-- Create a new table from the view
SELECT *
INTO dbo.listing_features
FROM dbo.vw_listing_features;
