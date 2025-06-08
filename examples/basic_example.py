import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio
import random
import time
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace import TracerProvider
from src.sysmon_autoinstumentor import SysmonAutoInstrumentor

# setup signoz exporter
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
otlp_exporter = OTLPSpanExporter(
    endpoint="http://localhost:4317",
    insecure=True
)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))

# setup python auto instrumentor
sysmon_autoinstumentor = SysmonAutoInstrumentor(tracer)
sysmon_autoinstumentor.instrument()

def main():
    time.sleep(0.5)
    main2()
    
def main2():
    time.sleep(0.5)
    asyncio.run(main5())
    
async def main4(random_times):
    await asyncio.sleep(random_times)
    
async def main5():
    random_times = [random.random() for _ in range(10)]
    tasks = [asyncio.create_task(main4(random_time)) for random_time in random_times]
    await asyncio.gather(*tasks)
    
main()

with tracer.start_as_current_span("root") as span:
    main()
        
        
        
        
        
        





