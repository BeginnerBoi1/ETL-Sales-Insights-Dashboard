USE etl_project;

CREATE VIEW summary_saless_2 AS
SELECT sales_data.`sub-category`,
		ROUND(SUM(sales_data.profit), 2) AS total_profit,
        AVG(sales_data.sales) AS avg_sales
FROM sales_data
GROUP BY sales_data.`sub-category`
ORDER BY ROUND(SUM(sales_data.profit), 2) DESC;

CREATE VIEW top_category AS
SELECT sales_data.category,
	   ROUND(SUM(sales_data.profit), 2) AS `Total Profit`
FROM sales_data
GROUP BY sales_data.category
ORDER BY  SUM(sales_data.profit) DESC;

CREATE VIEW total_profit AS
SELECT SUM(sales_data.profit)
FROM sales_data;

CREATE VIEW top_10_products AS
SELECT DISTINCT sales_data.product_name AS product, ROUND(SUM(sales_data.profit), 2)
FROM sales_data
GROUP BY sales_data.product_name
ORDER BY ROUND(SUM(sales_data.profit), 2) DESC
LIMIT 10;

CREATE VIEW regional_profit AS
SELECT sales_data.region,
	   ROUND(SUM(sales_data.profit)) AS profit
FROM sales_data
GROUP BY sales_data.region
ORDER BY ROUND(SUM(sales_data.profit));
		
