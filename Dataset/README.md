# **FROG**: **FR**amework of **O**pen **G**raphRAG
![frog-logo](https://github.com/user-attachments/assets/0119354b-7fe4-4232-9f26-8ff1122b4edd)

## Environment Setup
**Run all these commands below in the terminal.**<br>
Setup a new virtual environment.
```
python -m venv env
```
Activate the new virtual environment.
```
.\env\Scripts\activate
```
Install the requirements.
```
pip install -r requirements.txt
```
If you want to use Transformer's API, follow the instructions below.
- Change `.env.example` to `.env`
- Fill the environment variable with your HF Token, such as `HF_TOKEN=hf_snkdiNJinshJnjdndfjnaajn`

## Dataset Generation
To generate dataset, simply run the command below in the terminal.
```
python .\dataset\main.py [dataset_name] [dataset_path] [timeout] [amount] [category] [count]
```
The arguments are as follows.
- `dataset_name` is the name of the dataset. This will create a new subfolder within the `dataset/io/` with the name you define.
- `dataset_path` is the path to your dataset or the API endpoint for remote KG.
- `timeout` is the timeout limit for the system in generating an entry.
- `amount` is the amount of question-query pairs you want to generate.
- `category` is the category of the question. This can be `[simple|complex]_[1|2]`. Check our paper for the details.
- `count` is the flag indicating whether you want to generate count queries. Pass `--count` if you want to, otherwise leave it blank.

Example:
```
python .\dataset\main.py wikidata https://query.wikidata.org/sparql 40 10 complex_1
```
```
python .\dataset\main.py courses dataset\io\kg_courses.ttl 40 10 complex_1
```

To exclude some properties you do not want to include in the query, edit `dataset/io/excluded_props.txt` file. <br><br>
To define which classes you want to use (for DBpedia or Wikidata) in the query, edit `dataset/io/classes_allowed.txt` file. The system cannot randomly pick entities from the whole KG due to the size.