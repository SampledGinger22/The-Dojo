SELECT countries.name, languages.language, languages.percentage FROM languages
JOIN countries ON countries.id = country_id
WHERE languages.language = "Slovene"
order by languages.percentage desc;

SELECT countries.name, COUNT(*)
FROM cities
LEFT JOIN countries on cities.country_id = countries.id
GROUP BY countries.name
order by count(*) desc;

SELECT cities.name, cities.population FROM countries
LEFT JOIN cities ON cities.country_id = countries.id
WHERE countries.name = "Mexico" and cities.population > 500000;

SELECT countries.name, languages.language, languages.percentage FROM languages
LEFT JOIN countries ON countries.id = languages.country_id
WHERE languages.percentage > 89.0
ORDER BY percentage desc;

SELECT name, surface_area, population from countries
WHERE surface_area < 501 and population > 100000;

SELECT name, government_form, life_expectancy, capital from countries
WHERE government_form = "Constitutional Monarchy" and capital > 200 and life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population from countries
JOIN cities ON cities.country_id = countries.id
WHERE cities.district = "Buenos Aires" and cities.population > 500000;

SELECT region, COUNT(name) as "Countries"
FROM countries
GROUP BY region
order by count(*) desc;