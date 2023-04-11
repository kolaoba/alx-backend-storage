-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT
    band_name,
    COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY COALESCE(split, 2022) - formed DESC;