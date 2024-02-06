from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings


class VectorModelClass:

    def vectorLoadModel(self, question):
        from langchain_community.document_loaders import PyPDFLoader

        loader = PyPDFLoader("The Code on Wages 2019 No. 29 of 2019.pdf")
        pages = loader.load_and_split()

        vectorstore = Chroma.from_documents(documents=pages, embedding=GPT4AllEmbeddings())
        docs = vectorstore.similarity_search(question)
        len(docs)
        return docs
