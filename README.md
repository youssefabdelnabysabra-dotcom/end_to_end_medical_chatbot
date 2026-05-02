<<<<<<< HEAD
# end_to_end_medical_chatbot
# End-to-end Medical Chatbot (RAG)

This repository contains a Retrieval-Augmented Generation (RAG) medical chatbot built with LangChain, Pinecone, and Sentence-Transformers.

How to run
----------

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Create and activate a Conda environment (recommended):

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your credentials:

```ini
PINECONE_API_KEY=your_pinecone_key
OPENAI_API_KEY=your_openai_key
```

5. (Optional) Build and store embeddings in Pinecone:

```bash
python store_index.py
```

6. Start the web app:

```bash
python app.py
```

Open `http://localhost:8080` to interact with the chatbot.

Tech stack
----------
- Python
- LangChain
- Pinecone
- Hugging Face sentence-transformers
- Flask

Deployment notes
----------------
The repository includes guidance for building a Docker image and deploying to AWS (ECR + EC2) and for configuring GitHub Actions. Remember to set the following secrets in the GitHub repository for CI/CD:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ECR_REPO`
- `PINECONE_API_KEY`
- `OPENAI_API_KEY`
