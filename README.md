# Vault Primia — seu segundo cérebro

Uma pasta de notas para trabalhar com contexto: perfil do negócio, projetos, decisões e próximos passos. Obsidian organiza a leitura; Claude Code ajuda a trabalhar nos arquivos. Codex é complementar.

**[Comece aqui](COMECE-AQUI.md)**. A primeira entrega é uma nota revisada do primeiro projeto do seu negócio: oferta, público, problema e objetivo. Diário fica para a continuidade. O caminho serve a prestadores de serviço, negócios locais e infoprodutores.

## Antes do evento

Prepare VS Code, Obsidian, Claude Code e Live Server pelo [guia de preparação](https://segundo-cerebro-v2.vercel.app/). Você usa sua própria conta elegível. Codex é opcional. No Obsidian, basta abrir o aplicativo; o kit será obtido no encontro. ZIP de kit não instala aplicativos ou extensões.

## No encontro

1. Baixe o ZIP desta versão pelo GitHub (Code → Download ZIP), extraia numa pasta nova e abra a pasta que contém LEIA-ME.md no VS Code.
2. Abra essa mesma pasta como cofre no Obsidian. Não misture com acervo pessoal existente.
3. No painel do Claude Code, use `/setup`, revise o perfil e confirme antes de salvar.
4. Peça: **“Crie o primeiro projeto do meu negócio usando meu perfil. Registre o que ofereço, para quem, qual problema resolve e qual objetivo. Mostre para eu revisar antes de salvar.”**
5. Reabra a nota salva. Ela será a base para oferta, pesquisa, visual e página HTML local, conforme o ritmo da turma.

Se está revisando uma pull request, baixe o ZIP da branch da PR. A branch main só recebe as mudanças após merge. Não confunda uma branch acessível com a versão principal atualizada.

Alternativa assistida, sempre em pasta nova e vazia: peça ao assistente para baixar o ZIP de `berdantx/vault-primia`, explicar onde ficará e conferir que não há perfil/notas antes de extrair. Não sobrescreva um vault. O método recomendado não cria conexão Git; se já fez clone, nada apaga .git automaticamente.

## O que existe nesta revisão

- Perfil compartilhado em perfil.json e mapa de pastas, preservados ao repetir setup.
- Skills de projeto, oferta (expresso/completo/por etapa), pesquisa, concorrentes e direção visual.
- Inbox por demanda, abertura/fechamento do dia, reuniões, conteúdo, audiência, relatórios e propostas.
- Página local a partir da oferta ou reconstruída a partir de referência, sem herdar rastreadores.
- Bases oficiais frontend-design e theme-factory com licenças. Canvas-design é complemento opcional, não incluído no ZIP.
- Entradas para Claude Code e Codex apontando ao mesmo corpo de instruções, sem compartilhar memória interna automaticamente.
- Verificador opcional de preparação e auxiliares de perfil/projeto/HTML, somente locais. O percurso manual funciona sem Python.

Veja [rotinas](docs/ROTINAS.md), [instalação e recuperação](docs/INSTALACAO.md), [página local](docs/PAGINA-LOCAL.md), [licenças](docs/DESIGN-E-LICENCAS.md), [exemplos fictícios](exemplos/README.md) e [modelo sem IA](modelos/acompanhar-sem-ia.md).

## Limites claros

Não há monitoramento automático da inbox, instalação universal, transcrição de áudio garantida ou publicação incluída. Os 90 minutos não garantem pesquisa extensa, identidade completa e página final para todos. Scripts verificam invariantes; um teste real com iniciante continua necessário. As notas são locais, mas assistentes hospedados podem receber o contexto usado nos pedidos.

Nenhum plugin comunitário do Obsidian é obrigatório ou ativado pelo kit. A pasta .obsidian não é distribuída: preferências e plugins existentes não são sobrescritos.

Para desenvolvimento e testes: [MANUTENCAO](docs/MANUTENCAO.md). Não envie seu perfil ou suas notas ao repositório do template.
