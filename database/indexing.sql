-- Primary lookup column
CREATE NONCLUSTERED INDEX idx_listing_id
ON dbo.listing_features(listing_id);

-- If you frequently filter by host
CREATE NONCLUSTERED INDEX idx_host_id
ON dbo.listing_features(host_id);

-- If you filter by city/neighbourhood
CREATE NONCLUSTERED INDEX idx_property_city
ON dbo.listing_features(property_city);

CREATE NONCLUSTERED INDEX idx_property_neighbourhood
ON dbo.listing_features(property_neighbourhood);
