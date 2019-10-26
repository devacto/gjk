select order_date, no_of_service, sum(total_customer_per_order_type) as total_customer, order_type, total_customer_per_order_type, order_payment from (SELECT
  order_date,
  count_services_each_customer_each_day as no_of_service,
  all_services_each_customer_each_day as order_type,
  total_customer_per_order_type,
  CASE 
    WHEN all_payments_each_customer_each_day = ('GOPAY,CASH') THEN ('CASH,GOPAY')
    ELSE all_payments_each_customer_each_day
    END
  AS order_payment
FROM (
  SELECT order_date, all_services_each_customer_each_day, count_services_each_customer_each_day, all_payments_each_customer_each_day, count(customer_no) as total_customer_per_order_type
  FROM (
      SELECT
      DATE(order_time, "Asia/Jakarta") AS order_date,
      customer_no,
      STRING_AGG(DISTINCT order_type) AS all_services_each_customer_each_day,
      COUNT(DISTINCT order_type) AS count_services_each_customer_each_day,
      STRING_AGG(DISTINCT order_payment) AS all_payments_each_customer_each_day
      FROM (
        SELECT *
        FROM `bi-dwhdev-01.source.daily_order`
        where order_status = 'Completed'
        and order_time between TIMESTAMP('2018-04-07 00:00:00', "Asia/Jakarta") and TIMESTAMP('2018-04-08 00:00:00', "Asia/Jakarta")
        ORDER BY DATE(order_time, "Asia/Jakarta"), customer_no, order_type)
        GROUP BY DATE(order_time, "Asia/Jakarta"), customer_no)
  group by order_date, all_services_each_customer_each_day, count_services_each_customer_each_day, all_payments_each_customer_each_day
  ORDER BY order_date
  )
ORDER BY
  order_date,
  count_services_each_customer_each_day desc,
  all_payments_each_customer_each_day,
  all_services_each_customer_each_day) 
  group by order_date, no_of_service, order_type, total_customer_per_order_type, order_payment
  order by order_date, no_of_service asc;
