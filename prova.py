# alunos = []

# for i in range(0, 5):
#   nome = input(f"Digite o nome do aluno {i + 1}: ")
#   nota = float(input(f"Digite a nota de {nome}: "))

#   aluno = (nome, nota)

#   alunos.append(aluno)
  
# aluno_top = max(alunos, key=lambda x: x[1])
# print(f"O aluno com a maior nota é: {aluno_top[0]} com {aluno_top[1]} pontos!")

# ==================================================================
# dias_em_atraso = int(input("Quantos dias seu salário está atrasado: "))
# salario = float(input("Digite o valor do seu salário: "))
# multa_dia = salario * 0.02
# multa_total = 0

# if dias_em_atraso > 5:
#   for dia in range(6, dias_em_atraso + 1):
#     multa_total += multa_dia
#     print(f"Dia {dia} recebe multa. Valor acumulado de multa a receber = R${multa_total:.2f}")
#   print(f"Valor total a receber = R${salario + multa_total:.2f}")
# else:
#   print("Seu salário não esta atrasado!")

# -----------------------------------------------------------------
# teto = float(input("Digite o limite de gasto: R$"))

# quantidade_de_itens = 0
# total = 0

# for i in range(1, 5 + 1):
#   preco_item = float(input("Digite o preço do item: R$"))

#   if preco_item <= 0:
#     continue

#   quantidade_de_itens += 1
#   total += preco_item
#   print(f"Quantidade de itens regristrados = {quantidade_de_itens}")
#   print(f"Sua parcial é de: R${total:.2f}")

#   if i >= 5:
#     print(f"Limite máximo de 5 itens atingindo!")

#   if total >= teto:
#     print(f"Você chegou ao seu teto limite de R${teto}")
#     print(f"Seu total foi de R${total:.2f}")
#     print(f"Seu teto ficou = R${teto - total:.2f}")
#     break
  
# print(f"Total em reais acumulado = R${total:.2f}")
# print(f"Quantidade de itens computados = {quantidade_de_itens}")
# ---------------------------------------------------------------------

# alunos = []

# for i in range(3):
#   nome = input(f"Digite o nome do aluno {i + 1}: ")
#   notas = []
#   for j in range(3):
#     nota = float(input(f"Digite a nota {j + 1} de {nome}: "))
#     notas.append(nota)
  
#   alunos.append([nome, notas])

# medias = []
# for i in alunos:
#   print(f"Aluno: {i[0]}")
#   media = float(sum(i[1]) / len(i[1]))
#   print(f"A média é = {media:.2f}")
#   medias.append(media)

# media_geral =  sum(medias) / len(medias)

# print(f"A media geral dos alunos é = {media_geral:.2f}")

# maior_media = max(medias)
# indice_maior = medias.index(maior_media)
# aluno_top = alunos[indice_maior][0]

# print(f"O aluno com a maior nota é {aluno_top}, com {maior_media:.2f} pontos!")

# ==========================================================================================

# usuarios = {}

# while True:
#   print("Sistema de Login")
#   print("1 - Cadastrar usuário")
#   print("2 - Fazer login")
#   print("3 - Sair")
  
#   opcao = input("Escolha uma opção: ")

#   if opcao == "1":
#     nome = input("Digite um nome de usuário: ")
#     if nome in usuarios:
#       print("Usuário ja cadastrado!")
#     else:
#       senha = input("Digite uma senha: ")
#       usuarios[nome] = senha
#       print("Usuário cadastrado com sucesso!")
#   elif opcao == "2":
#     nome = input("Usuário: ")
#     if nome in usuarios:
#       senha = input("Senha: ")
#       if senha == usuarios[nome]:
#         print(f"Bem vindo, {nome}")
#       else:
#         print("Senha incorreta!")
#     else:
#         print("Usuário não encontrado!")  
#   elif opcao == "3":
#     print("Encerrando o sistema...")
#     break
#   else:
#     print("Opção inválida, tente novamente")  

# ==========================================================================================

# filmes = []

# for i in range(3):
#   titulo = input(f"Digite o nome do filme {i + 1}: ")
#   genero = input(f"Digite o gênero do filme {titulo}: ")
#   ano = int(input(f"Digite o ano de lançamento do filme {titulo}: "))
#   nota = float(input(f"Digite uma nota para o filme {titulo}: "))

#   filme = {
#     "titulo": titulo,
#     "genero": genero,
#     "ano": ano,
#     "nota": nota
#   }

#   filmes.append(filme)


# notas = []
# for i in filmes:
#   print("Filmes recomendados (nota maior que 8): ")
#   if i["nota"] >= 8:
#     print(f"Título: {i["titulo"]} - Nota: {i["nota"]}")

#   notas.append(i["nota"])
# # print(notas)
# media = sum(notas) / len(notas)
# print(f"A média das notas dos filmes cadastrados é: {media}")


filmes = []
while True:
  print("====Catálogo de Filmes====")
  print("1 - Cadastrar novos filmes")
  print("2 - Listar todos os filmes cadastrados")
  print("3 - Mostrar apenas os filmes recomendados (nota maior que 8)")
  print("4 - Exibir a média das notas dos filmes cadastrados")
  print("5 - Encerrar o programa")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    titulo = input(f"Digite o nome do filme: ")
    ja_existe = False
    
    for f in filmes:
      if f["titulo"].lower() == titulo.lower():
        ja_existe = True
        print("Filme já cadastrado")
        break  
    else:
      genero = input(f"Digite o gênero do filme {titulo}: ")
      ano = input(f"Digite o ano de lançamento do filme {titulo}: ")
      nota = float(input(f"Digite uma nota para o filme {titulo}: "))

    filme = {
      "titulo": titulo,
      "genero": genero,
      "ano": ano,
      "nota": nota
    }

    filmes.append(filme)
  
  elif opcao == "2":
    if len(filmes) > 0:
      for i in filmes:
        print(f"Filmes cadastrados: ") 
        print(f"Título: {i['titulo']} | Gênero: {i['genero']} | Ano: {i['ano']} | Nota: {i['nota']}")
    else:
      print("Não há filmes cadastrados!")

  elif opcao == "3":
    if len(filmes) == 0:
      print("Não há filmes cadastrados!")
    else:
      print("Filmes recomendados:")
      recomendados = []
      for i in filmes:
        if i["nota"] >= 8:
          recomendados.append(i)
          print(f"Título: {i['titulo']} - Nota: {i['nota']}")

  elif opcao == "4":
    notas = []
    for i in filmes:
      notas.append(i['nota'])
    media = sum(notas) / len(notas)
    print(f"A média das notas dos filmes cadastrados é: {media:.2f}")

  elif opcao == "5":
    print("Encerrando o sistema...")
    break
  else:
    print("Opção inválida, tente novamente.")







