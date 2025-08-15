import requests
import random

def get_word_and_data_from_api():
    # Palavras do jogo (não mostradas)
    game_words = ["python", "computador", "internet", "tecnologia", "programacao", "casa", "amor", "vida", "tempo", "mundo"]
    game_word = random.choice(game_words)
    
    # API apenas para dicas
    api_hint = None
    try:
        print("Buscando dica adicional da API...")
        response = requests.get("https://api.wordnik.com/v4/words.json/randomWord?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if 'word' in data:
                api_word = data['word'].lower()
                
                # Busca definição da palavra da API para usar como dica
                def_response = requests.get(f"https://api.wordnik.com/v4/word.json/{api_word}/definitions?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&limit=1", timeout=5)
                
                if def_response.status_code == 200:
                    def_data = def_response.json()
                    if def_data and len(def_data) > 0:
                        raw_definition = def_data[0].get('text', 'Palavra relacionada')
                        # Limpa tags XML e formata a definição
                        clean_definition = raw_definition.replace('<xref>', '').replace('</xref>', '').replace('<', '').replace('>', '')
                        # Limita tamanho da dica
                        if len(clean_definition) > 80:
                            clean_definition = clean_definition[:80] + "..."
                        api_hint = f"Dica da API: {clean_definition}"
                        print("Dica obtida da API com sucesso!")
                
    except Exception as e:
        print("Erro ao buscar dica da API (usando apenas dicas locais)")
    
    return game_word, api_hint

def get_word_hints(word, api_hint):
    hints = []
    
    # Dicas básicas
    hints.append(f"Palavra com {len(word)} letras")
    hints.append(f"Primeira letra: {word[0].upper()}")
    
    # Dica da API (sem revelar a palavra)
    if api_hint and "garlic press" not in api_hint.lower():
        hints.append(api_hint)
    elif api_hint:
        hints.append("Dica da API: Palavra em inglês relacionada")
    
    # Dicas específicas das palavras do jogo
    dicas_locais = {
        "python": "Linguagem de programação popular",
        "computador": "Máquina que processa dados",
        "internet": "Rede mundial de computadores",
        "tecnologia": "Aplicação de conhecimento científico",
        "programacao": "Arte de criar software",
        "casa": "Local onde se mora",
        "amor": "Sentimento de afeição",
        "vida": "Estado dos seres vivos",
        "tempo": "Duração das coisas",
        "mundo": "Planeta Terra"
    }
    
    if word in dicas_locais:
        hints.append(f"Significado: {dicas_locais[word]}")
    
    return hints

def show_progress(word, guessed):
    return ' '.join([letter if letter in guessed else '_' for letter in word])

def calculate_points(word_length, wrong_guesses, max_wrong, guess_type):
    base_points = word_length * 2
    penalty = wrong_guesses * 2
    bonus = 0
    
    if guess_type == "complete_word":
        bonus = 10
    elif wrong_guesses == 0:
        bonus = 5
    
    return max(base_points - penalty + bonus, 1)

print("JOGO DA FORCA COM DICAS!")
print("Sistema de Pontuacao:")
print("   - Pontos base: tamanho da palavra x 2")
print("   - Penalidade: -2 pontos por erro")
print("   - Bonus palavra completa: +10 pontos")
print("   - Bonus sem erros: +5 pontos")
print("   - Perder jogo: -5 pontos")

total_points = 0
games_played = 0

while True:
    games_played += 1
    word, api_hint = get_word_and_data_from_api()
    word = word.lower()
    hints = get_word_hints(word, api_hint)
    guessed_letters = set()
    wrong_count = 0
    max_wrong = 6
    guess_type = "letter_by_letter"
    
    print(f"\nNova palavra: {show_progress(word, guessed_letters)}")
    print(f"Tamanho: {len(word)} letras")
    print("\nDicas:")
    for i, hint in enumerate(hints, 1):
        print(f"   {i}. {hint}")
    
    while wrong_count < max_wrong:
        print(f"\n{show_progress(word, guessed_letters)}")
        print(f"Erros: {wrong_count}/{max_wrong}")
        
        guess = input("Digite uma letra ou palavra: ").lower().strip()
        
        if len(guess) == 1:
            if guess in guessed_letters:
                print("Ja tentou essa letra!")
                continue
            
            guessed_letters.add(guess)
            
            if guess in word:
                print(f"Acertou! '{guess}' esta na palavra")
                if all(letter in guessed_letters for letter in word):
                    round_points = calculate_points(len(word), wrong_count, max_wrong, guess_type)
                    total_points += round_points
                    print(f"Parabens! Palavra: {word}")
                    print(f"Pontos desta rodada: +{round_points}")
                    break
            else:
                print(f"'{guess}' nao esta na palavra")
                wrong_count += 1
        else:
            if guess == word:
                guess_type = "complete_word"
                round_points = calculate_points(len(word), wrong_count, max_wrong, guess_type)
                total_points += round_points
                print(f"Perfeito! Palavra: {word}")
                print(f"Pontos desta rodada: +{round_points}")
                break
            else:
                print(f"'{guess}' nao e a palavra")
                wrong_count += 1
    
    if wrong_count >= max_wrong:
        total_points -= 5
        print(f"Game Over! Palavra: {word}")
        print(f"Pontos perdidos: -5")
    
    print(f"Pontos totais: {total_points}")
    print(f"Jogos: {games_played} | Media: {total_points/games_played:.1f} pts/jogo")
    
    if input("\nJogar novamente? (s/n): ").lower() != 's':
        break

print(f"\nESTATISTICAS FINAIS:")
print(f"Pontuacao total: {total_points}")
print(f"Jogos jogados: {games_played}")
print(f"Media por jogo: {total_points/games_played:.1f} pontos")
print(f"{'Excelente!' if total_points/games_played > 10 else 'Bom trabalho!' if total_points/games_played > 5 else 'Continue praticando!'}")
print("Obrigado por jogar!")