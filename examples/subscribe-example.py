"""
Subscribe Example - Sync and Async

This example demonstrates how to use the subscribe method to start a virtual try-on prediction
and automatically poll for status updates until completion. It shows both synchronous and
asynchronous usage patterns.
"""

import os
import asyncio
from scribo_fashn_ai import ScriboFashnAI, AsyncScriboFashnAI

print("="*50)
print("SYNCHRONOUS EXAMPLE")
print("="*50)

client = ScriboFashnAI(
    api_key=os.environ.get("SCRIBO_FASHN_AI_API_KEY"), 
)

def on_enqueued(request_id: str) -> None:
    print(f"Prediction enqueued with ID: {request_id}")

def on_queue_update(status) -> None:
    print(f"Status update: {status.status}")
    if status.status == "processing":
        print("Your try-on is being processed...")
    elif status.status == "in_queue":
        print("Your try-on is in queue...")

try:
    response = client.run.subscribe(
        inputs={
            "garment_image": "https://lojafarm.vteximg.com.br/arquivos/ids/3531233-1416-2124/342595_51521_1-VESTIDO-LONGO-MG-BEATRICE-FLORAL.jpg?v=638739680281430000",
            "model_image": "https://lojafarm.vteximg.com.br/arquivos/ids/3531756-1416-2124/343131_51624_1-VESTIDO-MIDI-MALU.jpg?v=638739687435000000",
        },
        model_name="tryon-v1.6",
        pool_interval=1.0,  # Poll every 1 second
        timeout=120.0,      # Timeout after 2 minutes
        on_enqueued=on_enqueued,
        on_queue_update=on_queue_update,
    )
    
    print("Try-on completed!")
    print(f"Final status: {response.status}")
    if response.output:
        print(f"Output images: {response.output}")
    
except TimeoutError:
    print("The prediction timed out")
except RuntimeError as e:
    print(f"Prediction failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


# Async Example
print("\n" + "="*50)
print("ASYNC EXAMPLE")
print("="*50)

async_client = AsyncScriboFashnAI(
    api_key=os.environ.get("SCRIBO_FASHN_AI_API_KEY"),  # This is the default and can be omitted
)

def async_on_enqueued(request_id: str) -> None:
    print(f"[ASYNC] Prediction enqueued with ID: {request_id}")

def async_on_queue_update(status) -> None:
    print(f"[ASYNC] Status update: {status.status}")
    if status.status == "processing":
        print("[ASYNC] Your try-on is being processed...")
    elif status.status == "in_queue":
        print("[ASYNC] Your try-on is in queue...")

async def run_async_example():
    try:
        response = await async_client.run.subscribe(
            inputs={
                "garment_image": "https://lojafarm.vteximg.com.br/arquivos/ids/3531233-1416-2124/342595_51521_1-VESTIDO-LONGO-MG-BEATRICE-FLORAL.jpg?v=638739680281430000",
                "model_image": "https://lojafarm.vteximg.com.br/arquivos/ids/3531756-1416-2124/343131_51624_1-VESTIDO-MIDI-MALU.jpg?v=638739687435000000",
            },
            model_name="tryon-v1.6",
            pool_interval=1.0,  # Poll every 1 second
            timeout=120.0,      # Timeout after 2 minutes
            on_enqueued=async_on_enqueued,
            on_queue_update=async_on_queue_update,
        )
        
        print("[ASYNC] Try-on completed!")
        print(f"[ASYNC] Final status: {response.status}")
        if response.output:
            print(f"[ASYNC] Output images: {response.output}")
        
    except TimeoutError:
        print("[ASYNC] The prediction timed out")
    except RuntimeError as e:
        print(f"[ASYNC] Prediction failed: {e}")
    except Exception as e:
        print(f"[ASYNC] An error occurred: {e}")

# Run the async example
asyncio.run(run_async_example())