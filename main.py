import collections
# Abre os arquivos de leitura
trabalho_entrada = open("TCC_Cesar.txt", encoding="utf8")
palavra_comum_entrada = open("Common_Words.txt", encoding="utf8")

palavra_comum = set()  # Para armazenar as palavras, função set() pois não há necessidade de ser ordenada como a tupla
contador_words = {}  # Define o contador de palavras como um dict "palavra : quantidade no texto"


for line in palavra_comum_entrada:
    for word in line.split():
        palavra_comum.add(word.strip())  # "add" em palavra_comum set()

print(palavra_comum)

for line in trabalho_entrada:
    for word in line.split():

        word = word.lower().strip()
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace("–", "")



        if word.isdigit() is False:  # Verifica se a string não é um dígito
            if word not in palavra_comum:
                if word not in contador_words:
                    contador_words[word] = 1
                else:
                    contador_words[word] += 1



contar_dict = collections.Counter(contador_words)


for word, count in contar_dict.most_common(10):
    print(word, ":", count)

#O quarto maior valor é um espaço em branco, não consegui identificar o porquê, provavelmente é algo relacionado a formatação do texto