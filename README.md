# ChatGLM-Instruct-Tuning

基于清华的 [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) + Alpaca 方式进行finetune.

数据集: [中文alpaca](https://github.com/carbonz0/alpaca-chinese-dataset)


## 准备

### 安装依赖
```
pip install -r requirements.txt
```

### 下载数据
```
cd data
git clone https://github.com/carbonz0/alpaca-chinese-dataset
```

### 数据预处理


转化alpaca数据集为按行存储的Intruct格式数据

```bash
python cover_alpaca2jsonl.py
```

然后把数据划分为train.txt和valid.txt，保存在 ./data/example/路径下

### 训练


```bash
bash scripts/finetune.sh
```

### 推理
```
python infer.py
```