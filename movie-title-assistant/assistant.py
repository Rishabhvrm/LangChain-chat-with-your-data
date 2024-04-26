import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import streamlit as st


def create_movie_title(genre: str) -> str:
    """
    Generate a movie title based on the input genre.

    Args:
        genre (str): The genre for which the movie title is to be generated.

    Returns:
        str: The generated movie title.
    """
    # set values for key and model
    api_key = os.environ.get("OPENAI_API_KEY")
    model = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo", temperature=0.5)

    # prompt generation
    prompt_template = PromptTemplate(
        input_variables=['genre'],
        template="Create a movie title for the following genre: {genre}"
    )

    # chaining
    chain = prompt_template | model
    output = chain.invoke({"genre": genre})
    return output.content
    

def main():
    """
    A chatbot that works on one prompt at a time.
    Below, the context is set that it has to suggest a movie title based on user input genre.
    """
    # other example prompts: "Let me answer what's on your mind!"
    st.title("Let me create a movie title for you!")
    user_input_genre = st.text_input("Type the genre below:")

    # chain
    if user_input_genre:
        movie_title = create_movie_title(user_input_genre)
        st.write("Generated Movie Title:", movie_title)


if __name__ == "__main__":
    main()
