from secret_key import openAPI_key 
import os
os.environ['OPENAI_API_KEY']= openAPI_key
from langchain_openai import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

def generate(cuisine):
   
    llm = OpenAI(api_key=openAPI_key, model_name="gpt-3.5-turbo-instruct", temperature=0.6)

    prompt_template_names = PromptTemplate(
        input_variables=["cuisine"],
        template = "Come up with a fancy name for a {cuisine} restaurant that I will be starting in Barcelona."
        )

    name_chain = LLMChain(llm = llm, prompt = prompt_template_names, output_key = "restaurant_name") # used output key to store name

    prompt_template_menu = PromptTemplate(
        input_variables=["restaurant_name"],
        template = "Come up with a fancy menu items for restaurant {restaurant_name}. Return only 5 items as a comma seperated list and no need to explain what the items are just provide the names"
        )

    menu_chain = LLMChain(llm = llm, prompt = prompt_template_menu, output_key = "menu_items")


    result_chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables = ["cuisine"],
        output_variables = ["restaurant_name","menu_items"]
    )

    # need to use dictionary since there are multiple variables now so need to specify.
    result = result_chain({"cuisine": cuisine})
    #The result will be a dictionary which contains the name of the restaurant and it menu items
    return result

