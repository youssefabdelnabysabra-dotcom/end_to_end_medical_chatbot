"""
end to end process flow 
1. The system starts by loading PDF documents using the PDF loader

2. The loaded documents split into smaller chunks to improve processing

3. Each text chunk is converted to embedding 

4. The embeddings are stored in a Pinecone vector 

5. When a user ask a question, the retriever searches for
   the most relevant chunks from the database

6. The retrieved context is combined with the user query and passed to a language model

7. The model generates a concise answer based on the provided context

8. The final answer is returned to the user interface
"""