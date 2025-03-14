#!/bin/bash

# models=(
#     "mistralai/Mistral-Nemo-Instruct-2407"
#     "meta-llama/Llama-3.1-8B-Instruct"
#     "Qwen/Qwen2.5-Coder-7B-Instruct"
#     "Qwen/Qwen2.5-7B-Instruct"
# )

models=(
    "Qwen/Qwen2.5-3B-Instruct"
)

# models=(
#     "Qwen/Qwen2.5-Coder-7B-Instruct"
# )

# models=(
#     "meta-llama/Llama-3.1-8B-Instruct"
#     "Qwen/Qwen2.5-Coder-7B-Instruct"
#     "Qwen/Qwen2.5-7B-Instruct"
# )

# models=(
#     "mistralai/Mistral-Nemo-Instruct-2407"
# )


for model in "${models[@]}"; do
    echo "================================================================================"
    echo "Running evaluation for model: $model"
    echo "================================================================================"
    python eval.py \
        --knowledge-source="legal" \
        --model-name="$model" \
        --log-file-path="logs/log_$model.txt" \
        --test-df-path="data/eval/legal_test.json" \
        --llm-try-threshold=5 \
        --local-model \
        --no-local-weaviate-client \
        --use-cot \
        --max-new-tokens=1500 \
        --no-use-transform-factoid
    echo "================================================================================"
done
