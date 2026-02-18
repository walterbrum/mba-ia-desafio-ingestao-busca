from search import search_prompt

def main():
    print("Chat - desafio ingestão e busca! (digite 'sair' para sair)\n")
    while True:
        user_input = input("Digite sua pergunta: ")
        if user_input.lower() == "sair":
            print("Até logo!")
            break
        response = search_prompt(user_input)
        print(response)
        print("=" * 45)

if __name__ == "__main__":
    main()