# Average Selling Price — LeetCode #1251

## Intuition

We need to calculate the average selling price for each product based on the number of units sold at each price.
The selling price applies only when the purchase date falls within the product's price period.

## Approach

1. LEFT JOIN `Prices` with `UnitsSold` using `product_id`.
2. Match only the sales whose `purchase_date` falls between `start_date` and `end_date`.
3. Calculate the total revenue using `price * units`.
4. Divide total revenue by total units sold.
5. Use `COALESCE()` to return `0` when a product has no sales.
6. Round the result to 2 decimal places.
7. Group the result by `product_id`.

## Complexity

* Time: O(n × m)
* Space: O(n)

## SQL Concepts

* LEFT JOIN
* BETWEEN
* SUM()
* COALESCE()
* GROUP BY
* ROUND()
* Aggregate Functions

## Key Learning

When calculating an average selling price with different prices and quantities, use total revenue divided by total units sold.

## Code

```sql
SELECT p.product_id,
       ROUND(
           COALESCE(SUM(p.price * u.units) / SUM(u.units), 0),
           2
       ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
```
