Create a model-and-data governance starter for SoberFuture.me.

You must define:
- which model tasks are allowed
- which tasks require retrieval grounding
- which tasks require human review
- which tasks are prohibited
- what datasets are needed for evaluation
- how to separate operational data from evaluation data
- how to de-identify sensitive data
- how to log model behavior safely
- how to benchmark hallucination, tone, faithfulness, and escalation behavior

Include:
- prompt registry design
- evaluation dataset schema
- annotation guidance
- safety test cases
- offline eval plan
- online monitoring plan
- rollback plan for bad prompts or models
