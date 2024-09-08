def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
"05 de Setembro de 2024",
"De tudo, ao meu amor serei atento",
"Antes, e com tal zelo, e sempre, e tanto",
"Que mesmo em face do maior encanto",
"Dele se encante mais meu pensamento.",
"Quero vivê-lo em cada vão momento",
"E em louvor hei de espalhar meu canto",
"E rir meu riso e derramar meu pranto",
"Ao seu pesar ou seu contentamento.",
"E assim, quando mais tarde me procure",
"Quem sabe a morte, angústia de quem vive",
"Quem sabe a solidão, fim de quem ama",
"Eu possa me dizer do amor (que tive):",
"Que não seja imortal, posto que é chama",
"Mas que seja infinito enquanto dure.",
autor="Vinicius de Moraes",
ano=1990,
)
