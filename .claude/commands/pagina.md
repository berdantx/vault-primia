---
description: Cria uma página pronta (captura, obrigado, vendas) já com o seu texto e sua cara
---

Crie uma página web completa para o dono deste vault. Ele não é programador: ele descreve o que quer e recebe a página funcionando.

## PASSO 1 — Entender o essencial (no máximo 3 perguntas)

Leia o `CLAUDE.md` (negócio, público, tom de voz) e `lancamentos/` antes de perguntar qualquer coisa. Depois pergunte só o que faltar:

1. Qual o objetivo da página? (capturar contato, vender, agradecer, apresentar)
2. O que a pessoa ganha? (a oferta, o evento, o material)
3. Para onde vai o botão? (WhatsApp, checkout, formulário)

Se ele já disse tudo isso no pedido, não pergunte nada. Vá direto para o passo 2.

## PASSO 2 — Escrever o texto antes do código

Escreva a copy primeiro, no tom de voz dele:
- **Título:** a promessa mais concreta possível. Nada de "transforme sua vida".
- **Subtítulo:** para quem é e o que vai acontecer.
- **3 a 5 blocos** de benefício, sempre em resultado, não em característica.
- **Prova:** depoimento, número, resultado real. Se não houver, deixe o espaço marcado como `[COLOCAR DEPOIMENTO AQUI]` e avise.
- **Chamada para ação:** verbo no imperativo, primeira pessoa. "Quero minha vaga" funciona melhor que "Enviar".

## PASSO 3 — Montar a página

Um único arquivo `.html`, com tudo dentro (CSS e imagens em base64 ou de link público). Nada de instalar nada.

Regras de design que não se negociam:
- **O botão principal precisa gritar.** Fundo sólido na cor de destaque, texto contrastante, sombra colorida, letra grande e em negrito. Se ele passa despercebido numa olhada de 2 segundos, está errado.
- Funciona no celular primeiro. A maioria vai abrir pelo telefone.
- Fonte grande (16px ou mais no corpo), espaçamento generoso, no máximo 2 famílias de fonte.
- Uma cor de destaque só, usada com parcimônia.
- Sem travessão na copy.

## PASSO 4 — Entregar

1. Salve em `lancamentos/[nome-do-projeto]/` (crie a pasta se não existir).
2. Abra a página no navegador para ele ver.
3. Diga onde salvou e liste em uma linha o que ele precisa trocar: link do botão, depoimento, foto.
4. Ofereça: "quer que eu publique isso na internet com um link real?" e só publique se ele pedir.
