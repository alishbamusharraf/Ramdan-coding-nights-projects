# Import the chainlit library and alias it as 'cl'
import chainlit as cl
# Decorator to handle incoming messages
@cl.on_message
# Define an async function that takes a message parameter
async def main(message: cl.Message):

    response = f"You said: {message.content}"

    await cl.Message(content=response).send()