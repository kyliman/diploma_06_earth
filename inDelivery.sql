select
    "Couriers"."login",
    count("Orders"."id")
from "Couriers"
inner join "Orders" on "Orders"."courierId" = "Couriers"."id"
where "Orders"."inDelivery" = true
and "Orders"."cancelled" = false
and "Orders"."finished" = false
group by "Couriers"."id";