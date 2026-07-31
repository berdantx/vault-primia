# Vault Primia — Seu Segundo Cérebro

Um comando. Um segundo cérebro montado no seu computador.

Este repositório é um **vault Obsidian pronto**: estrutura de pastas, regras de trabalho e comandos de IA já configurados. O Claude lê essas regras e passa a trabalhar como um braço direito que conhece o seu negócio.

## Como instalar

**1.** Abra o VS Code em uma pasta vazia (File → Open Folder) e abra o Claude na barra lateral.

**2.** Cole esta linha no Claude e mande:

```
Baixe o conteúdo do vault https://github.com/berdantx/vault-primia direto NESTA pasta que já está aberta, sem criar subpasta, e me guie na instalação.
```

**3.** Quando terminar, rode:

```
/setup
```

O Claude vai te entrevistar em texto livre, montar o vault personalizado para o seu negócio e deixar tudo pronto para usar.

**4.** Abra a mesma pasta no Obsidian (Open folder as vault) e pronto: suas notas com cara de app, e o Claude trabalhando dentro delas.

> **Por que colar a linha em vez de usar `git clone`?** Porque o `git clone` cria uma subpasta nova com o nome do repositório, e aí o VS Code fica aberto um nível acima do vault: nenhum comando funciona e aparece "comando não existente". A linha acima baixa tudo direto na pasta que você já abriu.
>
> Se você preferir mesmo usar o terminal, o comando que instala na pasta atual (sem criar subpasta) é:
> ```
> git clone https://github.com/berdantx/vault-primia .
> ```
> O ponto no final é o que faz a diferença: significa "aqui mesmo". A pasta precisa estar vazia.

> Pré-requisitos: VS Code com a extensão Claude Code (plano Pro ou Max) e Obsidian instalados. Passo a passo completo em **[aula-setup-primia.vercel.app](https://aula-setup-primia.vercel.app)**.

## O que vem dentro

| Pasta | Para que serve |
|---|---|
| `inbox/` | Zona de entrada: tudo novo cai aqui e é processado depois |
| `diario/` | Um arquivo por dia: foco, pendências, registros |
| `conteudo/` | Ideias, roteiros, transcrições (é aqui que o Claude aprende seu tom de voz) |
| `lancamentos/` | Cada lançamento ou projeto grande em sua subpasta |
| `alunos/` | Alunos, mentorados ou clientes: histórico e próximos passos |
| `reunioes/` | Resumos de calls processadas pelo `/reuniao` |
| `pesquisa/` | Referências, swipes e materiais de estudo |
| `pessoal/` | Metas, saúde, finanças, vida fora do trabalho |
| `arquivo/` | Trabalho concluído. Nunca deletado, só movido |

Cada pasta tem um `_sobre.md` com a regra dela, que o Claude lê e respeita.

## Comandos

| Comando | O que faz |
|---|---|
| `/setup` | Monta o vault: entrevista você e preenche o CLAUDE.md (rode uma vez) |
| `/diario` | Abre o dia: revisa pendências e define o foco |
| `/tldr` | Fecha a sessão: salva o resumo na pasta certa |
| `/conteudo` | Cria ideias e roteiros no seu tom de voz |
| `/humanizar` | Tira a cara de IA de qualquer texto |
| `/pagina` | Cria uma página pronta: captura, obrigado, vendas |
| `/publicar` | Coloca a página no ar com um link real, de graça |
| `/reuniao` | Transcrição de call vira decisões e próximos passos |
| `/audiencia` | Comentários e pesquisas viram direção de conteúdo e oferta |

## O arquivo mais importante

O `CLAUDE.md` é o contrato: quem você é, o que faz, seu público, seu tom de voz e as regras da casa. O Claude lê esse arquivo em toda conversa, e é por isso que ele "te conhece" desde a primeira mensagem. O `/setup` preenche ele para você.

## Manual completo

Instalação detalhada, o que dá para fazer com cada pasta, exemplos de pedidos prontos e as regras de ouro:

**[aula-setup-primia.vercel.app/manual](https://aula-setup-primia.vercel.app/manual)**

---

Feito pela [Primia](https://primia.ai) · IA que aguenta lançamento
