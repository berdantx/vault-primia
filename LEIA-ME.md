# Bem-vindo ao seu Segundo Cérebro 🧠

Este é o seu vault: uma pasta de arquivos de texto que vira a memória central do seu negócio. O Obsidian mostra essas notas de forma bonita, e o Claude trabalha dentro delas com você.

## ⚠️ Antes de tudo: abra a PASTA CERTA

Os comandos (`/setup`, `/diario`) só funcionam se o VS Code estiver aberto **exatamente nesta pasta**, a que contém este arquivo LEIA-ME.md.

**Como conferir em 5 segundos:** na barra lateral esquerda do VS Code você tem que ver `CLAUDE.md`, `LEIA-ME.md` e as pastas `inbox`, `diario`, `conteudo`. Se em vez disso você vê **o nome de uma pasta só** (com tudo isso dentro dela), você está um nível acima. Feche e abra de novo em File → Open Folder, entrando nessa pasta.

**Quem usou `git clone` cai nisso sempre:** o git cria uma subpasta nova com o nome do repositório. Se você rodou o clone dentro de `meus-projetos`, o vault ficou em `meus-projetos/vault-primia`. É essa pasta de dentro que você abre no VS Code, não a de fora.

> Digitou `/setup` e apareceu "comando não existente"? É isso: pasta errada. Não é erro seu nem do sistema.

## Primeiros passos (faça nessa ordem)

1. **Abra esta pasta no VS Code** (File → Open Folder) e abra o Claude pela barra lateral.
2. **Digite `/setup`** na conversa. O Claude vai te entrevistar em texto livre e montar o vault pra você: preenche o CLAUDE.md com quem você é, ajusta as pastas pro seu contexto e deixa tudo pronto. É um comando só.
3. **No dia seguinte, digite `/diario`.** É assim que seu dia começa daqui pra frente.
4. A partir daí, é conversa em português. Peça o que você pediria a um braço direito.

> Prefere fazer manual? Abra o `CLAUDE.md` e preencha os campos `[PREENCHA]` você mesmo. O `/setup` faz exatamente isso, só que entrevistando você.

## As pastas e o que vai em cada uma

| Pasta | O que vai aqui |
|---|---|
| `inbox/` | Tudo que chega e ainda não tem lugar. Processar e esvaziar sempre. |
| `diario/` | Um arquivo por dia: foco, pendências, o que aconteceu. |
| `conteudo/` | Ideias, roteiros, carrosséis, calendário editorial. |
| `lancamentos/` | Cada lançamento ou projeto grande tem sua subpasta. |
| `alunos/` | Seus alunos, mentorados ou clientes: histórico e próximos passos. |
| `reunioes/` | Resumos de calls e reuniões, gerados pelo `/reuniao`. |
| `pesquisa/` | Referências, swipes, materiais de estudo. |
| `pessoal/` | Metas, saúde, finanças, vida fora do trabalho. |
| `arquivo/` | Tudo que acabou. Nunca delete: mova pra cá. |

Cada pasta tem um arquivo `_sobre.md` explicando as regras dela. Pode renomear as pastas para o seu contexto (ex: `alunos/` virar `clientes/`), só avise o Claude para atualizar o `CLAUDE.md`.

## Comandos prontos

**Comece por estes:**
- `/setup` monta o vault pra você: entrevista em texto livre e preenche tudo (rode uma vez, no começo).
- `/diario` abre o seu dia: lê pendências, revisa o que ficou de ontem e define o foco.
- `/tldr` fecha a sessão: salva um resumo do que foi feito na pasta certa.

**Para produzir:**
- `/conteudo` gera ideias e roteiros no seu tom de voz.
- `/humanizar` tira a cara de IA de qualquer texto (cole o texto e mande).
- `/pagina` cria uma página pronta: captura, obrigado, vendas.
- `/publicar` coloca a página no ar com um link real, de graça.

**Para inteligência do negócio:**
- `/reuniao` transforma transcrição de call em decisões e próximos passos, e ainda atualiza a ficha do aluno.
- `/audiencia` lê comentários, DMs ou respostas de pesquisa e mostra o que seu público está pedindo.

## Regra de ouro

O sistema só funciona com uso diário. Rode `/diario` toda manhã por 7 dias seguidos e você não vai mais conseguir trabalhar sem.
