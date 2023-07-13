select "Orders"."track",
case
    when "Orders"."finished" = true
        then 2
    when "Orders"."cancelled" = true
        then -1
    when "Orders"."inDelivery" = true
        then 1
    else 0
end status
from "Orders";