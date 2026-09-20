# AI/ML + GenAI + Agentic AI — 12-Day Industry Workshop

> **Duration:** 12 Days  
> **Recommended effort:** 3–4 hours/day  
> **Learning model:** 30% concepts + 70% hands-on  
> **Goal:** Build an industry-style AI/ML + GenAI + Agentic AI project and learn how an AI solution is designed, developed, tested, deployed and presented.

---

## Why I am doing this workshop

The biggest risk is **passive attendance**. Listening to a mentor for 12 days will not make me stand out or become one of the 10–20 students selected for an internship.

My strategy is:

1. Understand the concept the same day.
2. Build the practical task instead of only watching it.
3. Ask at least one useful question every day.
4. Explain one concept aloud to the mentor/team.
5. Keep GitHub commits organized.
6. Maintain a daily learning log.
7. Build reusable notes, code and diagrams.
8. Connect every concept to a real business problem.
9. Prepare a final project that I can explain without reading slides.
10. Practice a 2–3 minute technical explanation every day.

---

# 12-Day Workshop Roadmap

| Day | Module | Main Topics | Practical Output |
|---|---|---|---|
| 1 | AI & ML Industry Overview | AI/ML/DL landscape, use cases, lifecycle, careers | First AI application + environment |
| 2 | Python for AI/ML | NumPy, Pandas, processing, visualization | Dataset analysis |
| 3 | Data Engineering for ML | Cleaning, preprocessing, feature engineering, EDA | Real-world dataset prepared |
| 4 | Machine Learning | Regression, classification, clustering | ML prediction model |
| 5 | Advanced ML | Random Forest, XGBoost concepts, feature selection, tuning, CV | Optimized model |
| 6 | Deep Learning | ANN, CNN, NLP fundamentals | Deep-learning model |
| 7 | Generative AI | LLMs, Transformers, tokens, embeddings, prompting, hallucination, safety | GenAI application |
| 8 | RAG & AI Applications | Embeddings, vector DBs, document processing, RAG | College/Company RAG chatbot |
| 9 | Agentic AI Fundamentals | Agents, reasoning, planning, memory, tools, function calling | Basic AI Agent |
| 10 | Advanced Agentic AI | Multi-agent systems, workflows, orchestration, autonomous tasks | Multi-step AI Agent |
| 11 | Industry AI Project | Architecture, APIs, FastAPI, Git/GitHub, deployment, testing, monitoring | Complete AI solution |
| 12 | Demo & Hackathon | Presentation, business impact, architecture, scalability | Final demo + presentation |

---

# Daily Preparation Plan

## Day 1 — AI & ML Industry Overview

### Learn
- AI vs ML vs Deep Learning
- Generative AI vs traditional ML
- Industry use cases:
  - fraud detection
  - recommendation systems
  - predictive maintenance
  - healthcare
  - customer support
  - document intelligence
  - cybersecurity
- AI project lifecycle:
  `Problem → Data → EDA → Features → Model → Evaluation → Deployment → Monitoring`
- AI engineering roles and skills

### Practical
Set up:
- Python
- VS Code
- Jupyter Notebook
- Git/GitHub
- virtual environment
- required Python packages

Create your first small AI application.

### Example
For credit-card fraud:

`Transaction data → preprocessing → ML model → fraud probability → alert`

### Dry run
If a transaction has:
- amount = ₹50,000
- unusual location
- unusual time
- unusual merchant

The model uses these features to estimate whether the transaction is likely fraudulent.

### Ask the mentor
> "In a real company, how do you decide whether a problem should use traditional ML, deep learning, or an LLM?"

### Daily confidence task
Explain AI vs ML vs DL in 60 seconds without notes.

---

## Day 2 — Python for AI/ML

### Learn
- NumPy arrays
- Pandas Series/DataFrame
- loading CSV
- filtering
- grouping
- missing values
- basic statistics
- Matplotlib/visualization

### Practical
Take a real dataset and answer:
- How many rows?
- How many columns?
- Which columns are numeric?
- Which contain missing values?
- Which feature has the largest variation?
- What patterns are visible?

### Example
```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.describe())
```

### Dry run
If the dataset contains 1,000 transactions and 10 columns:

`df.shape → (1000, 10)`

If `Amount` has 20 missing values:

`df["Amount"].isnull().sum() → 20`

### Ask the mentor
> "When working with a large production dataset, what changes compared with using Pandas on a small CSV?"

### Confidence task
Show the mentor one useful observation you discovered from the dataset.

---

## Day 3 — Data Engineering for ML

### Learn
- data cleaning
- duplicate removal
- missing-value handling
- outlier detection
- encoding categorical features
- feature scaling
- feature engineering
- train/test split
- EDA

### Practical pipeline
`Raw Data → Clean → Transform → Features → Train/Test Data`

### Example
If:
- Age = 20
- Salary = ₹500,000
- City = Jaipur

Possible transformations:
- scale Age and Salary
- one-hot encode City
- create `income_per_age`

### Dry run
Before:
`City = Jaipur`

After one-hot encoding:
`City_Jaipur = 1`

### Ask the mentor
> "Which preprocessing steps should be fitted only on training data, and why?"

### Confidence task
Explain data leakage and give one example.

---

## Day 4 — Machine Learning

### Learn
- supervised learning
- unsupervised learning
- regression
- classification
- clustering
- train/test split
- prediction
- evaluation

### Algorithms
**Regression**
- Linear Regression

**Classification**
- Logistic Regression
- KNN
- Decision Tree

**Clustering**
- K-Means

### Example
Predict house price:

`Area + Bedrooms + Location → Price`

### Dry run
Suppose a trained regression model predicts:

Actual = ₹50 lakh  
Predicted = ₹47 lakh

Absolute error:

`|50 - 47| = ₹3 lakh`

### Classification example
Actual:
`Fraud = 1`

Prediction:
`Fraud probability = 0.87`

If threshold = 0.50:

`0.87 > 0.50 → Fraud`

### Ask the mentor
> "How do you choose an evaluation metric when the classes are highly imbalanced?"

### Confidence task
Explain the difference between regression and classification.

---

## Day 5 — Advanced ML

### Learn
- Random Forest
- boosting
- XGBoost concepts
- feature importance
- feature selection
- hyperparameter tuning
- cross-validation
- overfitting vs underfitting

### Practical
Train a baseline model and then improve it.

Compare:
`Baseline → Tuned Model`

### Dry run: Cross-validation
With 5-fold CV:

`Fold 1 → validation`
`Fold 2 → validation`
`Fold 3 → validation`
`Fold 4 → validation`
`Fold 5 → validation`

Average the five validation scores.

### Important metrics
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- MAE
- MSE
- RMSE

### Ask the mentor
> "When would you choose a simpler model instead of XGBoost or another more complex model?"

### Confidence task
Explain overfitting using a real-world analogy.

---

## Day 6 — Deep Learning

### Learn
- neuron
- weights
- bias
- activation function
- forward propagation
- loss
- backpropagation
- epochs
- batch size
- ANN
- CNN
- NLP fundamentals

### Simple neuron
`z = w1x1 + w2x2 + b`

Then:

`output = activation(z)`

### Dry run
Suppose:

`x1 = 2`
`x2 = 3`
`w1 = 0.5`
`w2 = 0.2`
`b = 1`

Then:

`z = (0.5×2) + (0.2×3) + 1`
`z = 2.6`

The activation function converts this into the neuron's output.

### CNN idea
For an image:
`Image → convolution → feature maps → pooling → classification`

### Ask the mentor
> "What type of problems genuinely require deep learning instead of a traditional ML model?"

### Confidence task
Draw and explain a simple neural network.

---

## Day 7 — Generative AI Fundamentals

### Learn
- LLMs
- Transformers
- tokens
- embeddings
- attention
- prompting
- context
- hallucination
- temperature
- AI safety
- structured outputs

### Basic architecture
`User → Prompt → LLM → Response`

### Example prompt
Bad:
> "Tell me about resumes."

Better:
> "Analyze this resume for a backend developer role. Identify 5 missing technical skills and explain each recommendation in one sentence."

### Dry run
Input:
> "What skills should a Python backend developer learn?"

The model:
1. tokenizes the prompt
2. processes context
3. predicts likely next tokens
4. generates the response

### Hallucination example
If an LLM invents a library, statistic or citation that is not supported by evidence, that is a hallucination.

### Ask the mentor
> "How do production AI systems reduce hallucinations when the answer must be factually reliable?"

### Confidence task
Show the mentor a weak prompt and your improved version.

---

## Day 8 — RAG & AI Applications

### Learn
- document processing
- chunking
- embeddings
- vector databases
- semantic search
- retrieval
- generation
- RAG architecture

### RAG pipeline
`Documents → Chunking → Embeddings → Vector DB`

Then:

`User Question → Query Embedding → Retrieval → Context → LLM → Answer`

### Example
College policy PDFs are uploaded.

Question:
> "What is the attendance requirement?"

RAG retrieves the relevant section and gives it to the LLM.

### Dry run
If 100 pages are split into chunks:

`100 pages → many text chunks → embeddings → vector database`

Query:
`"attendance requirement"`

The system finds the most semantically relevant chunks instead of sending all 100 pages to the model.

### Ask the mentor
> "How do you decide chunk size and retrieval count in a production RAG system?"

### Confidence task
Draw the RAG architecture on paper and explain every component.

---

## Day 9 — Agentic AI Fundamentals

### Learn
- AI agent
- chatbot vs agent
- reasoning
- planning
- memory
- tools
- function calling
- task execution

### Chatbot
`Question → Answer`

### Agent
`Goal → Plan → Tool → Observe → Next Action → Result`

### Example
User:
> "Find the best time for my meeting tomorrow and prepare an email."

An agent could:
1. inspect calendar
2. find available slots
3. select a slot based on rules
4. draft the email
5. ask for approval before sending

### Dry run
Goal:
`Calculate today's sales and summarize them.`

Agent:
`Get data → calculate → analyze → generate summary`

### Ask the mentor
> "What is the boundary between an AI agent and a normal workflow with an LLM call?"

### Confidence task
Explain agent vs chatbot in under 90 seconds.

---

## Day 10 — Advanced Agentic AI

### Learn
- multi-agent systems
- specialized agents
- orchestration
- workflows
- tool use
- autonomous task execution
- error handling
- human-in-the-loop

### Example
Research system:

`Planner Agent`
↓
`Research Agent`
↓
`Data Analysis Agent`
↓
`Writer Agent`
↓
`Reviewer Agent`

### Dry run
Task:
> "Prepare a market research report."

1. Planner creates tasks.
2. Researcher gathers information.
3. Analyst processes the information.
4. Writer creates the report.
5. Reviewer checks the result.

### Ask the mentor
> "When does a multi-agent system add real value, and when does it only add unnecessary complexity?"

### Confidence task
Draw the agent workflow and identify one failure point.

---

## Day 11 — Industry AI Project

### Learn
- system architecture
- REST APIs
- FastAPI
- Git/GitHub
- environment variables
- testing
- deployment
- monitoring
- logging

### Suggested architecture

```text
Frontend
   ↓
FastAPI Backend
   ↓
AI/ML Service
   ↓
Database / Vector DB / External APIs
```

### Git workflow
```bash
git init
git add .
git commit -m "initial project"
git branch
git status
git push
```

### FastAPI concept
```python
@app.post("/predict")
def predict(data: InputData):
    result = model.predict(...)
    return {"prediction": result}
```

### Project checklist
- clear problem statement
- dataset/data source
- architecture diagram
- model/LLM choice
- API
- frontend or usable interface
- testing
- GitHub repository
- README
- deployment plan
- limitations
- future improvements

### Ask the mentor
> "If this project had 10,000 users, which component would you redesign first?"

### Confidence task
Give a 2-minute architecture explanation.

---

## Day 12 — Industry Demo & Hackathon

### Presentation structure

**1. Problem — 30 sec**
What real problem are you solving?

**2. Solution — 45 sec**
What did you build?

**3. Architecture — 45 sec**
How does the system work?

**4. Demo — 2–3 min**
Show the actual workflow.

**5. AI/ML — 45 sec**
Why did you choose this model/LLM/RAG/agent architecture?

**6. Business impact — 30 sec**
What time, cost or effort could this reduce?

**7. Limitations — 20 sec**
What does the system not solve?

**8. Future scope — 20 sec**
What would you improve next?

### Final questions to prepare
- Why this problem?
- Why this model?
- Why not another model?
- What data did you use?
- How did you evaluate it?
- What happens when the model is wrong?
- How do you handle security?
- How does it scale?
- What is the biggest limitation?
- What would you build next?

---

# Daily Mentor Interaction System

Use this every day.

### Before the session — 20–30 minutes
- Read the day's topics.
- Write 3 questions.
- Review yesterday's code.
- Identify one thing you do not understand.

### During the session
- Ask one technical question.
- Ask one industry/application question.
- Write down one mentor insight.
- Volunteer for at least one explanation/demo.

### After the session — 30–60 minutes
- Rebuild the practical task yourself.
- Commit code to GitHub.
- Write 5 bullet points of learning.
- Write tomorrow's questions.

---

# Daily Question Bank

## Day 1
1. How does a company decide whether AI is actually needed?
2. What is the difference between an ML engineer and an AI engineer?
3. What makes an AI project production-ready?

## Day 2
1. When is Pandas insufficient for large-scale data?
2. How do you handle missing data in production?
3. Which visualization is useful for detecting outliers?

## Day 3
1. What is data leakage?
2. Why should scaling be fitted on training data?
3. How do you detect bad features?

## Day 4
1. How do you choose regression vs classification?
2. Why can accuracy be misleading?
3. When is clustering useful?

## Day 5
1. Why does cross-validation help?
2. How does Random Forest reduce overfitting?
3. What does feature importance tell us?

## Day 6
1. Why use CNNs for images?
2. What causes vanishing/exploding gradients?
3. How do epochs and batch size affect training?

## Day 7
1. Why do LLMs hallucinate?
2. What is the practical purpose of embeddings?
3. How can prompt design improve output reliability?

## Day 8
1. Why use RAG instead of putting all documents into a prompt?
2. What makes a good chunk?
3. How do you evaluate retrieval quality?

## Day 9
1. What makes an agent different from a chatbot?
2. When should an agent ask a human for approval?
3. How should tool failures be handled?

## Day 10
1. Why use multiple agents?
2. What causes agent loops?
3. How do you monitor an autonomous workflow?

## Day 11
1. How should an AI API be secured?
2. What should be logged in production?
3. How would you scale the architecture?

## Day 12
1. What is the business value of the project?
2. What is the biggest technical limitation?
3. What would you change if you had another month?

---

# GitHub Repository Structure

```text
ai-ml-genai-agentic-ai-workshop/
│
├── README.md
├── requirements.txt
│
├── day-01-ai-ml-overview/
│   ├── notes/
│   └── practical/
│
├── day-02-python-ai-ml/
│   ├── notebooks/
│   └── dataset/
│
├── day-03-data-engineering/
├── day-04-machine-learning/
├── day-05-advanced-ml/
├── day-06-deep-learning/
├── day-07-generative-ai/
├── day-08-rag/
├── day-09-agentic-ai/
├── day-10-advanced-agents/
├── day-11-industry-project/
│
├── day-12-demo/
│   ├── presentation/
│   ├── demo/
│   └── final-report/
│
└── final-project/
    ├── frontend/
    ├── backend/
    ├── models/
    ├── data/
    ├── tests/
    └── README.md
```

---

# Git Commit Strategy

Do not dump 12 days of work into one commit.

Use meaningful commits:

```text
Day 01: setup environment and first AI application
Day 02: add dataset analysis
Day 03: add preprocessing pipeline
Day 04: train baseline ML model
Day 05: optimize model and evaluate
Day 06: add deep learning experiment
Day 07: add GenAI application
Day 08: implement RAG pipeline
Day 09: implement basic agent
Day 10: add multi-step agent workflow
Day 11: expose AI system through FastAPI
Day 12: finalize demo and documentation
```

---

# Personal Selection Strategy

If only 10–20 interns are selected, do not try to impress mentors by talking constantly.

Instead, create evidence of capability:

- consistent attendance
- clean GitHub commits
- working practicals
- useful questions
- ability to explain concepts
- debugging ability
- teamwork
- initiative
- final project quality
- clear technical communication

The strongest signal is not:

> "I know AI."

It is:

> "Here is what I built, here is why I designed it this way, here is how I tested it, and here is what I would improve."

---

# Final 12-Day Checklist

- [ ] Environment configured
- [ ] GitHub repository created
- [ ] Daily code committed
- [ ] Daily notes maintained
- [ ] Dataset analyzed
- [ ] ML model trained
- [ ] Model optimized
- [ ] Deep-learning experiment completed
- [ ] GenAI application completed
- [ ] RAG chatbot completed
- [ ] AI agent completed
- [ ] Multi-step agent completed
- [ ] FastAPI/API integrated
- [ ] Final project documented
- [ ] Architecture diagram prepared
- [ ] Demo rehearsed
- [ ] 2-minute project explanation ready
- [ ] Technical Q&A practiced

---

# One Rule for the Workshop

**Do not leave a day with only notes. Leave every day with a working artifact.**
