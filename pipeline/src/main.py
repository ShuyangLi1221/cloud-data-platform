from pipeline.runner import PipelineRunner

from pipeline.customer import CustomerPipeline
from pipeline.product import ProductPipeline
from pipeline.order import OrderPipeline
from pipeline.order_item import OrderItemPipeline

from analytics.runner import AnalyticsRunner



def main():
  
    PipelineRunner.run(CustomerPipeline)

    PipelineRunner.run(ProductPipeline)

    PipelineRunner.run(OrderPipeline)

    PipelineRunner.run(OrderItemPipeline)
    
    AnalyticsRunner.run()



if __name__ == "__main__":
    main()