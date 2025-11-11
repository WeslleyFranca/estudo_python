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
        break
      if ja_existe:
        print("Filme ja cadastrado!")  

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
    if len(filmes) == 0:
      print("Não há filmes cadastrados!")
    else:
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







