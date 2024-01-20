from telegram.ext import CallbackQueryHandler, ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters 
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import openai

# Set OpenAI API key
openai.api_key = 'YOUR_KEY'

# Load prompts from file
with open('question.txt', 'r', encoding='utf-8') as f:
    prompts = f.read()

# Define a function to generate a response from OpenAI
def get_bot_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

async def ask(update, context):
    # Get the user's question from the command
    question = " ".join(update.message.text.split()[1:])
    # Generate a prompt to send to OpenAI
    prompt = f"\nHuman: {question}\nAI:"
    # Get the response from OpenAI
    response = get_bot_response(prompts + prompt)
    # Send the response back to the user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

if __name__ == "__main__":
    app = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()
    app.add_handlers(
        [
            CommandHandler('ask', ask), 
        ]
    )
    app.run_polling()







    
