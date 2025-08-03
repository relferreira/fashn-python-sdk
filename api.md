# Run

Types:

```python
from scribo_fashn_ai.types import RunPredictResponse, RunSubscribeParams
```

Methods:

- <code title="post /run">client.run.<a href="./src/scribo_fashn_ai/resources/run.py">predict</a>(\*\*<a href="src/scribo_fashn_ai/types/run_predict_params.py">params</a>) -> <a href="./src/scribo_fashn_ai/types/run_predict_response.py">RunPredictResponse</a></code>
- <code title="post /run + polling">client.run.<a href="./src/scribo_fashn_ai/resources/run.py">subscribe</a>(\*\*<a href="src/scribo_fashn_ai/types/run_subscribe_params.py">params</a>) -> <a href="./src/scribo_fashn_ai/types/status_retrieve_response.py">StatusRetrieveResponse</a></code>

# Status

Types:

```python
from scribo_fashn_ai.types import StatusRetrieveResponse
```

Methods:

- <code title="get /status/{id}">client.status.<a href="./src/scribo_fashn_ai/resources/status.py">retrieve</a>(id) -> <a href="./src/scribo_fashn_ai/types/status_retrieve_response.py">StatusRetrieveResponse</a></code>

# Credits

Types:

```python
from scribo_fashn_ai.types import CreditRetrieveBalanceResponse
```

Methods:

- <code title="get /credits">client.credits.<a href="./src/scribo_fashn_ai/resources/credits.py">retrieve_balance</a>() -> <a href="./src/scribo_fashn_ai/types/credit_retrieve_balance_response.py">CreditRetrieveBalanceResponse</a></code>
