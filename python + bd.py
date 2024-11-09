import mysql.connector

def buscar_jogos(palavra_chave):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bialins12062006",
            database="banco_jogos"
        )

        cursor = conn.cursor()

        query = "SELECT titulo, subtitulo FROM jogos WHERE titulo LIKE %s OR subtitulo LIKE %s"
        cursor.execute(query, (f"%{palavra_chave}%", f"%{palavra_chave}%"))
        resultados = cursor.fetchall()
        if resultados:
            print(f"Jogos que contêm '{palavra_chave}':")
            for titulo, subtitulo in resultados:
                print(f" - Título: {titulo}, Subtítulo: {subtitulo}")
        else:
            print(f"Nenhum jogo encontrado contendo '{palavra_chave}'.")

        cursor.execute("SELECT titulo, subtitulo FROM jogos ORDER BY titulo ASC")
        jogos_ordenados = cursor.fetchall()
        print("\nJogos em ordem crescente pelo título:")
        for titulo, subtitulo in jogos_ordenados:
            print(f" - Título: {titulo}, Subtítulo: {subtitulo}")

        query_k = "SELECT titulo, subtitulo FROM jogos WHERE titulo LIKE '%k%' OR subtitulo LIKE '%k%'"
        cursor.execute(query_k)
        jogos_com_k = cursor.fetchall()
        print("\nJogos que contêm 'k' no título ou subtítulo:")
        for titulo, subtitulo in jogos_com_k:
            print(f" - Título: {titulo}, Subtítulo: {subtitulo}")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

palavra_chave = input("Digite uma palavra-chave para buscar jogos: ")
buscar_jogos(palavra_chave)

