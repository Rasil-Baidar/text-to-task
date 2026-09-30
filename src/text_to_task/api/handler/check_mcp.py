from ollama import chat


async def check_mcp_handler(text: str) -> bool:
    response = chat(
        model='llama3.1',
        messages=[
            {"role": "user", "content": text}
        ]
    )
    print(response)
    return response.message.content