from services.customer_service import CustomerService
from services.order_service import OrderService
from services.order_item_service import OrderItemService

print("Generating daily customers...")
CustomerService.generate_daily()

print("Generating daily orders...")
OrderService.generate_daily()

print("Generating daily order items...")
OrderItemService.generate_daily()

print("Done.")