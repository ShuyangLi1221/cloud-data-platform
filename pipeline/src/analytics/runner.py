from analytics.sales import SalesAnalytics
from analytics.daily_sales import DailySalesAnalytics
from analytics.top_products import TopProductsAnalytics
from analytics.top_customers import TopCustomersAnalytics
from analytics.category_sales import CategorySalesAnalytics


class AnalyticsRunner:

    analytics = [
        SalesAnalytics,
        DailySalesAnalytics,
        TopProductsAnalytics,
        TopCustomersAnalytics,
        CategorySalesAnalytics,
    ]

    @classmethod
    def run(cls):
        for analytic in cls.analytics:
            analytic.run()