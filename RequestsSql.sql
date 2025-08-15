--Запрос1 Выведите все уникальные названия продуктов
SELECT distinct product_name FROM products

--Запрос2 Выведите id, название и стоимость продуктов с содержанием клетчатки (fiber) более 5 граммов.
SELECT p.product_id AS "product_id", "product_name", "price"
FROM products AS p
JOIN nutritional_information AS ni
ON p.product_id = ni.product_id
WHERE ni.fiber>5

--Запрос3 Выведите название продукта с самым высоким содержанием белка (protein)
SELECT p.product_name  
FROM products AS p  
JOIN nutritional_information AS ni 
ON p.product_id = ni.product_id  
ORDER BY ni.protein DESC  
LIMIT 1

--Запрос4 Подсчитайте общую сумму калорий для продуктов каждой категории,
-- но не учитывайте продукты с нулевым жиром (fat = 0). Выведите id категории, сумму калорий.
SELECT c.category_id, SUM(p.calories) AS "total_calories"  
FROM products AS p  
JOIN categories AS c 
ON p.category_id = c.category_id  
JOIN nutritional_information AS ni 
ON p.product_id = ni.product_id  
WHERE ni.fat > 0  
GROUP BY c.category_id

--Запрос5 Рассчитайте среднюю цену товаров каждой категории. Выведите название категории, среднюю цену.
SELECT c.category_name, AVG(p.price) AS "average_price"  
FROM products AS p  
JOIN categories AS c 
ON p.category_id = c.category_id  
GROUP BY c.category_name
