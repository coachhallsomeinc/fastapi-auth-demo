from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json

cloud_config= {
  'secure_connect_bundle': 'secure-connect-ripple-ai.zip'
}

with open("ripple_ai-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]
ASTRA_DB_KEYSPACE = "database"
OPENAI_API_KEY = "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"

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# this is creating memory of the story and saving it for 60 mins
message_history = CassandraChatMessageHistory(
    session_id = "ripplesession",
    session = session,
    keyspace = ASTRA_DB_KEYSPACE,
    ttl_seconds = 3600
)

message_history.clear()

cass_buff_memory = ConversationBufferMemory(
    memory_key = "chat_history",
    chat_memory = message_history
)

#template given to AI 
template = """
In a world where time travel is possible, you discover a mysterious journal that allows you to revisit pivotal moments in your life. However, each alteration you make has unforeseen consequences, creating a ripple effect that changes your present reality.

You start with a choice: travel back to a traumatic event in your childhood and prevent it, potentially erasing years of pain, or let the past remain unchanged and focus on your present life. The journal warns that altering the past may lead to unintended and unpredictable outcomes.

As you delve deeper into your own history, you face increasingly difficult decisions. Do you mend broken relationships, pursue missed opportunities, or right past wrongs? Each choice alters the course of your life in unexpected ways.

Your goal is to navigate this temporal labyrinth and reach a resolution. Will your journey through time lead to a brighter, happier existence, or will the ever-expanding butterfly effect result in a darker, more twisted reality? The power to shape your destiny is in your hands, but be cautious – the consequences of playing with time are profound and irreversible.

Here are some rules to follow:
1. Always begin by asking for a name.
2. Always end each response with a question for the user.
3. Stories should lead to an ending, whether that be good or bad.

Here is the chat history, use this to understand what to say next: {chat_history}
Human: {human_input}
AI:
"""

#setting input variables for ai prompt template
prompt = PromptTemplate(
    input_variables = ["chat_history", "human_input"],
    template = template
)

#initializing connection to openai
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
llm_chain = LLMChain(
    llm = llm,
    prompt = prompt,
    memory = cass_buff_memory
)

choice = "start"

while True: 
    response = llm_chain.predict(human_input=choice)
    print(response.strip())

    choice = input("Your reply: ")