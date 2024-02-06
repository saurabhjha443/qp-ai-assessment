
from Conversation import VectorModelClass


qa_chain = VectorModelClass()

qa_chain_object = qa_chain.vectorLoadModel


def generateResponseFromVectorObject(prompt):
    response = qa_chain_object(prompt)
    return response


if __name__ == "__main__":
    prompt = input("Enter a Prompt")
    result = generateResponseFromVectorObject(prompt)
    print(result)
