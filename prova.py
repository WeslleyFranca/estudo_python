# PROJETO CATÁLOGO DE FILMES
# filmes = []
# while True:
#   print("====Catálogo de Filmes====")
#   print("1 - Cadastrar novos filmes")
#   print("2 - Listar todos os filmes cadastrados")
#   print("3 - Mostrar apenas os filmes recomendados (nota maior que 8)")
#   print("4 - Exibir a média das notas dos filmes cadastrados")
#   print("5 - Encerrar o programa")

#   opcao = input("Escolha uma opção: ")

#   if opcao == "1":
#     titulo = input(f"Digite o nome do filme: ")
#     ja_existe = False
    
#     for f in filmes:
#       if f["titulo"].lower() == titulo.lower():
#         ja_existe = True
#         break
#       if ja_existe:
#         print("Filme ja cadastrado!")  

#     genero = input(f"Digite o gênero do filme {titulo}: ")
#     ano = input(f"Digite o ano de lançamento do filme {titulo}: ")
#     nota = float(input(f"Digite uma nota para o filme {titulo}: "))

#     filme = {
#       "titulo": titulo,
#       "genero": genero,
#       "ano": ano,
#       "nota": nota
#     }

#     filmes.append(filme)
  
#   elif opcao == "2":
#     if len(filmes) > 0:
#       for i in filmes:
#         print(f"Filmes cadastrados: ") 
#         print(f"Título: {i['titulo']} | Gênero: {i['genero']} | Ano: {i['ano']} | Nota: {i['nota']}")
#     else:
#       print("Não há filmes cadastrados!")

#   elif opcao == "3":
#     if len(filmes) == 0:
#       print("Não há filmes cadastrados!")
#     else:
#       print("Filmes recomendados:")
#       recomendados = []
#       for i in filmes:
#         if i["nota"] >= 8:
#           recomendados.append(i)
#           print(f"Título: {i['titulo']} - Nota: {i['nota']}")

#   elif opcao == "4":
#     if len(filmes) == 0:
#       print("Não há filmes cadastrados!")
#     else:
#       notas = []
#       for i in filmes:
#         notas.append(i['nota'])
#       media = sum(notas) / len(notas)
#       print(f"A média das notas dos filmes cadastrados é: {media:.2f}")

#   elif opcao == "5":
#     print("Encerrando o sistema...")
#     break
#   else:
#     print("Opção inválida, tente novamente.")
# ================================================================
# fUNÇÕES

# def exibir_produto (nome, preco):
#   return f"O produto {nome}, custa R${preco}"

# nome = input("Digite o nome do produto: ")
# price = float(input("Digite o preço do produto: "))

# resultado = exibir_produto(nome=nome, preco=price)

# print(resultado)
# ========================================================

# def calcular_desconto(preco, desconto):
#   valor_desconto = preco * (desconto / 100)
#   preco_final = preco - valor_desconto
#   return f"O valor final com desconto é R${preco_final:.2f}"

# resultado = calcular_desconto(1000, 20)

# print(resultado)
# =========================================================

# def celsius_para_fahrenheit(celsius):
#   to_fah = (celsius * 9/5) + 32
#   return f"{celsius}°C equivale a {to_fah}°F"

# ask_user = int(input("Digite a temperatura em Celsius: "))
# print(celsius_para_fahrenheit(ask_user))
# ==========================================================

# def imposto_sobre_salario(bruto, imposto=15):
#   calc = bruto * (imposto / 100)
#   liquido = bruto - calc
#   return f"Valor de imposto a ser pago = R${calc:.2f},\n salario liquido = R${liquido:.2f}"

# print(imposto_sobre_salario(3000, 20))
# ===========================================================

# def calcular_media(notas):
#   return sum(notas) / len(notas)

# def aprovado_reprovado(media):
#   if media < 7:
#     print("Reprovado")
#   else:
#     print("Aprovado")

# notas = []
# for i in range(1, 5):
#   nota = float(input(f"Digite sua nota {i}: "))
#   notas.append(nota)

# media = calcular_media(notas)
# print(f"Sua média foi {media:.1f}")
# aprovado_reprovado(media)
# =======================================================
# MÉTODO FILTER

# linguagens = ["Python", "JavaScript", "C", "Java", "Go", "Ruby"]
# maiores_de_4 = list(filter(lambda x: len(x) > 4, linguagens))
# print(maiores_de_4)
# ========================================================
# MÉTODO MAP

# celsius = [0, 10, 20, 30, 40]
# para_fah = list(map(lambda f: f * 1.8 + 32, celsius))
# print(para_fah)
# =======================================================
# USANDO MAP E FILTER

# precos = [100, 250, 50, 400, 75, 300]
# acima_100 = list(filter(lambda x: x > 100, precos))
# desconto = list(map(lambda x: x * 0.9, acima_100))
# print(desconto)








