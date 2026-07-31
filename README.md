# Vault Primia — Seu Segundo Cérebro

Um comando. Um segundo cérebro montado no seu computador.

Este repositório é um **vault Obsidian pronto**: estrutura de pastas, regras de trabalho e comandos de IA já configurados. O Claude lê essas regras e passa a trabalhar como um braço direito que conhece o seu negócio.

## Como instalar

**1.** Abra o VS Code em uma pasta vazia (File → Open Folder) e abra o Claude na barra lateral.

**2.** Cole esta linha no Claude e mande:

```
Baixe o vault de https://github.com/berdantx/vault-primia para esta pasta e me guie na instalação.
```

**3.** Quando terminar, rode:

```
/setup
```

O Claude vai te entrevistar em texto livre, montar o vault personalizado para o seu negócio e deixar tudo pronto para usar.

**4.** Abra a mesma pasta no Obsidian (Open folder as vault) e pronto: suas notas com cara de app, e o Claude trabalhando dentro delas.

> Pré-requisitos: VS Code com a extensão Claude Code (plano Pro ou Max) e Obsidian instalados. Passo a passo completo em **[aula-setup-primia.vercel.app](https://aula-setup-primia.vercel.app)**.

## O que vem dentro

| Pasta | Para que serve |
|---|---|
| `inbox/` | Zona de entrada: tudo novo cai aqui e é processado depois |
| `diario/` | Um arquivo por dia: foco, pendências, registros |
| `conteudo/` | Ideias, roteiros, transcrições (é aqui que o Claude aprende seu tom de voz) |
| `lancamentos/` | Cada lançamento ou projeto grande em sua subpasta |
| `alunos/` | Alunos, mentorados ou clientes: histórico e próximos passos |
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

## O arquivo mais importante

O `CLAUDE.md` é o contrato: quem você é, o que faz, seu público, seu tom de voz e as regras da casa. O Claude lê esse arquivo em toda conversa, e é por isso que ele "te conhece" desde a primeira mensagem. O `/setup` preenche ele para você.

## Manual completo

Instalação detalhada, o que dá para fazer com cada pasta, exemplos de pedidos prontos e as regras de ouro:

**[aula-setup-primia.vercel.app/manual](https://aula-setup-primia.vercel.app/manual)**

---

Feito pela [Primia](https://primia.ai) · IA que aguenta lançamento
