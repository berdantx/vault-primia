---
description: Coloca sua página no ar com um link real, de graça
---

O dono deste vault criou uma página (normalmente com `/pagina`) e quer colocar no ar. Ele não é técnico: conduza tudo, um passo de cada vez, e nunca despeje comando técnico sem explicar o que é.

## PASSO 1 — Achar a página

Procure o arquivo `.html` que ele quer publicar, geralmente em `lancamentos/`. Se houver mais de um, pergunte qual. Se não houver nenhum, sugira criar com `/pagina` primeiro.

## PASSO 2 — Conferir antes de subir

Abra o arquivo e confira, sem perguntar:
- Sobrou algum `[COLOCAR ALGO AQUI]` no texto?
- O botão principal tem link de verdade, ou está vazio?
- Tem erro de português ou nome escrito errado?

Se achar algo, avise em uma lista curta e pergunte se ele quer corrigir antes de publicar. Publicar com placeholder na tela é vergonha na frente do cliente dele.

## PASSO 3 — Publicar

Use a Vercel, que é gratuita para esse uso. Explique em uma linha o que vai acontecer antes de rodar qualquer coisa.

1. Verifique se a Vercel CLI está instalada e se ele está logado.
2. Se não estiver, guie a instalação e o login: o login abre o navegador, ele entra com o e-mail ou GitHub e volta.
3. Publique a pasta que contém a página.
4. Se o arquivo não se chamar `index.html`, renomeie a cópia publicada para `index.html`, senão o link não abre direto.

Se ele preferir não instalar nada, ofereça a alternativa: publicar pelo site da Vercel arrastando a pasta, ou usar o Netlify Drop. Explique o caminho em 3 passos.

## PASSO 4 — Entregar o link

1. Teste o link antes de mandar: ele precisa abrir e mostrar a página certa.
2. Entregue o link em uma linha, destacado, pronto pra copiar.
3. Diga como atualizar depois: "me peça pra publicar de novo e eu atualizo esse mesmo link".
4. Registre o link no arquivo do projeto em `lancamentos/`, para não se perder.

## Cuidados

- Nunca publique nada de `pessoal/`, `alunos/` ou `reunioes/`. São dados privados. Se o pedido envolver essas pastas, recuse e explique por quê.
- Antes de publicar qualquer coisa que tenha dado de aluno, nome de cliente ou número de faturamento, avise que aquilo vai ficar público na internet e confirme se é isso mesmo.
