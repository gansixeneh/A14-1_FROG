#!/bin/bash

models=(
    "nvidia/Mistral-NeMo-12B-Instruct"
    "meta-llama/Llama-3.1-8B-Instruct"
    "Qwen/Qwen2.5-Coder-7B-Instruct"
    "Qwen/Qwen2.5-7B-Instruct"
)

for model in "${models[@]}"; do
    echo "================================================================================"
    echo "Running evaluation for model: $model"
    echo "================================================================================"
    python eval.py \
        --knowledge-source="legal" \
        --model-name="$model" \
        --log-file-path="logs/log_$model.txt" \
        --test-df-path="FROG/data/eval/legal_test.json" \
        --llm-try-threshold=5 \
        --local-model \
        --no-local-weaviate-client \
        --use-cot \
        --max-new-tokens=300
    echo "================================================================================"
done
