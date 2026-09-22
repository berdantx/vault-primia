# Comece aqui

## 1. Confira os programas, uma coisa por vez

- Abra VS Code. Se faltar, use o [download oficial](https://code.visualstudio.com/download).
- Abra Obsidian. A tela inicial serve para esta conferência. [Download oficial](https://obsidian.md/download).
- No VS Code, Extensões → Claude Code for VS Code, publicador Anthropic. Instale/habilite se faltar, entre na sua conta elegível e envie: “Responda em português para confirmar meu acesso. Não altere arquivos.” Marque este passo só se recebeu resposta.
- Em Extensões, confira Live Server, publicador Ritwick Dey. Instale/habilite se faltar. Testaremos Go Live quando houver página.

Faça você as instalações e o login, seguindo as telas oficiais. Não compartilhe senha ou código. O [guia de preparação](https://segundo-cerebro-v2.vercel.app/) detalha Windows e Mac, custos/acesso e Codex opcional. A extensão não garante que o comando de terminal exista, e esse comando não é requisito aqui.

O auxiliar de conferência em docs/INSTALACAO.md é opcional. Sem ele, estes quatro testes manuais bastam. O kit não instala nada ao abrir uma pasta.

## 2. Abra a pasta do kit no encontro

Extraia o ZIP em uma pasta nova. No VS Code, Arquivo → Abrir Pasta: escolha a pasta que contém LEIA-ME.md. No Obsidian, Open folder as vault (Abrir pasta como cofre): escolha exatamente a mesma pasta. Não importe por cima de notas existentes.

Peça ao Claude Code: “Leia o LEIA-ME.md e me explique o que há nesta pasta, sem alterar arquivos.” Confira que a resposta corresponde ao kit aberto.

## 3. Conte sobre seu negócio

Digite `/setup`. Informe o que já sabe: negócio, público, oferta/serviço ou produto a desenvolver, região pertinente, objetivos e tom. Pode dizer “a definir”. Revise o rascunho e confirme antes de salvar perfil.json.

Se já existe perfil, ele deve ser lido e preservado. Repetir setup não apaga nem reinicia sua base. Ajustes de perfil e reorganização de pastas são revisados antes de alterar.

## 4. Crie o primeiro projeto do seu negócio

Cole no painel:

> Use meu perfil e crie o primeiro projeto do meu negócio. Quero trabalhar um serviço que já presto ou um produto que desejo desenvolver. Aproveite as informações já salvas e pergunte só o que falta. Registre o que ofereço, para quem, qual problema resolve e qual objetivo do projeto. Separe definido, hipótese e pendência. Mostre para eu revisar e, após minha confirmação, salve a nota e informe onde ficou.

Escolha algo pequeno e real. Reabra a nota no Obsidian. Ela deve ter os quatro pontos, próximo passo e caminho informado pelo assistente. Essa é a entrega essencial da prática.

## 5. Avance pelo seu ritmo

Use `/oferta expresso` para organizar a oferta; `/pesquisa` ou `/concorrentes` para perguntas de mercado; `/direcao-visual` para prévia e identidade aprovada; `/pagina` para HTML local. Cada etapa lê o projeto anterior. No modo completo, retome em outras sessões sem repetir a entrevista.

Para página, abra apenas a pasta site em outra janela do VS Code, nunca o vault inteiro, e use Live Server. Formulário sem integração é demonstração, não envio. Publicação não faz parte da oficina.

Ao terminar, `/tldr` deixa o registro. Em outro dia, `/diario` ajuda a retomar mesmo que ainda exista pouco histórico.

## Se algo travar

Anote programa, passo e mensagem exibida; peça apoio. Preencha [o mesmo exercício sem IA](modelos/acompanhar-sem-ia.md) em papel, documento ou notas do celular enquanto acompanha. [Recuperação](docs/INSTALACAO.md) explica os casos comuns.
