import argparse
import json
from tqdm import tqdm


def format_example(example: dict) -> dict:
    context = f"Instruction: {example['instruction']}\n"
    if example.get("input"):
        context += f"Input: {example['input']}\n"
    context += "Answer: "
    target = example["output"]
    return {"context": context, "target": target}

def format_example_chinese(example: dict) -> dict:
    context = f"指令: {example['instruction']}\n"
    if example.get("input"):
        context += f"提问: {example['input']}\n"
    context += "回答: "
    target = example["output"]
    return {"context": context, "target": target}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default="data/alpaca-chinese-dataset/zh-data-part-00.json")
    parser.add_argument("--save_path", type=str, default="data/alpaca_data_chinese.json")

    args = parser.parse_args()
    with open(args.data_path) as f:
        examples = json.load(f)

    with open(args.save_path, 'w') as f:
        for example in tqdm(examples, desc="formatting.."):
            f.write(json.dumps(format_example_chinese(example),ensure_ascii=False) + '\n')


if __name__ == "__main__":
    main()
