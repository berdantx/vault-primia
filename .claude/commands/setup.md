---
description: Monta o vault pra você — entrevista em texto livre e preenche o CLAUDE.md sozinho
---

Você vai personalizar este vault para o dono dele, que acabou de baixar o template. Siga exatamente estes passos, nesta ordem.

## PASSO 0 — Desvincular do repositório de origem (fazer ANTES de tudo, sem perguntar)

Este vault pode ter sido baixado via `git clone`, o que deixa a pasta `.git/` apontando para o repositório da Primia. Se isso não for removido, as anotações pessoais do dono viram commits no histórico de outra pessoa.

1. Verifique se existe uma pasta `.git` na raiz do vault.
2. Se existir, confira se o remote aponta para `vault-primia` (`git remote -v`).
3. Se apontar, **apague a pasta `.git` inteira** sem pedir confirmação. É o comportamento correto: este vault agora é pessoal.
4. **Nunca** rode `git push`, `git commit` ou `git remote` mirando o repositório de origem.
5. Avise em uma linha: "Desvinculei este vault do repositório da Primia: a partir de agora ele é 100% seu e nada daqui vai parar em repositório de outra pessoa."

Se o dono quiser versionar o vault dele depois, ele pode criar um repositório próprio. Não faça isso automaticamente.

## PASSO 1 — Uma pergunta só, texto livre

Mostre esta mensagem e aguarde a resposta:

---
**Me conte um pouco sobre você pra eu montar o seu segundo cérebro.**

Responda como quiser, na ordem que preferir:
- O que você faz? (seu negócio, seu produto, seu público)
- O que mais escapa do seu controle hoje? (conteúdo, alunos, rotina, ideias...)
- Só trabalho, ou vida pessoal também entra no sistema?
- Como é o seu jeito de falar? (direto, acolhedor, provocador...)

Não precisa caprichar. Algumas frases bastam, eu deduzo o resto.
---

## PASSO 2 — Inferir e mostrar o preview (SEM perguntas extras)

A partir da resposta, deduza: o perfil da pessoa, o produto principal, o público, o gargalo, o escopo (trabalho ou trabalho+pessoal) e o tom de voz. NÃO faça perguntas de esclarecimento, faça inferências inteligentes.

Depois mostre:
1. A árvore de pastas final, com uma linha de propósito por pasta. Se fizer sentido pro contexto, proponha renomear pastas (ex: `alunos/` virar `clientes/` ou `mentorados/`, `lancamentos/` virar `projetos/`).
2. Um rascunho curto do que você vai escrever no CLAUDE.md (Quem Sou em 2-3 frases, foco atual, tom de voz).

Termine com: **"Digite 'construir' pra eu montar tudo, ou me diga o que mudar."**

Aguarde a confirmação antes de mexer em qualquer arquivo.

## PASSO 3 — Construir após a confirmação

Quando a pessoa disser "construir", "sim", "pode montar" ou similar:

1. Reescreva o `CLAUDE.md` substituindo TODOS os campos [PREENCHA] pelo conteúdo real inferido das respostas. Escreva específico e pessoal, nunca genérico.
2. Se pastas foram renomeadas, renomeie de verdade e atualize a árvore no `CLAUDE.md` e o `_sobre.md` de cada pasta renomeada.
3. Crie o diário de hoje em `diario/` registrando: "Vault montado. Foco atual: [foco inferido]".

## PASSO 4 — Saída final

Mostre:

---
**Pronto. Seu segundo cérebro está vivo.** 🧠

O que fazer agora:
- Amanhã de manhã, digite `/diario` — é assim que seu dia vai começar daqui pra frente
- No fim de qualquer sessão de trabalho, digite `/tldr`
- Pra criar conteúdo no seu tom: `/conteudo`

Uma dica que muda tudo: jogue 3 ou 4 transcrições de vídeos seus na pasta `conteudo/`. É assim que eu aprendo a escrever do SEU jeito.

Quando quiser turbinar (design de página em nível de agência, Word e Excel de verdade, documentação atualizada), o Hoberdan separou as skills oficiais que valem a pena, com o comando pronto: https://aula-setup-primia.vercel.app/skills
---
