-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT
    band_name,
    COALESCE(split, CURRENT_DATE) - formed AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY COALESCE(split, CURRENT_DATE) - formed DESC;