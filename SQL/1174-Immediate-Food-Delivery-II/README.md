# Immediate Food Delivery II — LeetCode #1174

## Intuition

We need to find the percentage of customers whose **first order was delivered immediately**.

For each customer, we first find their earliest `order_date`. Then we check whether that first order's `order_date` is the same as the `customer_pref_delivery_date`.

## Approach

1. Find the earliest `order_date` for each customer using `MIN(order_date)`.
2. Use `GROUP BY customer_id` to find the first order of every customer.
3. Use `(customer_id, order_date) IN (...)` to keep only those first orders.
4. Use `CASE` to return:

   * `1` if the first order was immediate.
   * `0` otherwise.
5. Use `AVG()` to calculate the percentage of immediate first orders.
6. Multiply by `100` and round the result to 2 decimal places.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(n)**

## Code

```mysql id="c4r8kp"
# Write your MySQL query statement below

SELECT 
    ROUND(
        AVG(
            CASE 
                WHEN order_date = customer_pref_delivery_date 
                THEN 1 
                ELSE 0 
            END
        ) * 100, 
        2
    ) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);
```

## Key Learning

A **subquery with `MIN()` and `GROUP BY`** can be used to find the first record for each customer.

`CASE + AVG()` is a useful pattern for calculating the **percentage of rows satisfying a condition**.
